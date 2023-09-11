from Alphabet import Alphabet
import main as m
import re

def process_set(alphabets):
    
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    all_alphabets = re.findall(pattern, alphabets)
    
    for sets in all_alphabets:
        name = sets[0]  # Nombre del conjunto
        values = re.findall(r'[^,\s]+', sets[1])  # Lista de valores del conjunto
        Alphabet.add_alphabet(name, values)
        
        
def show_all_alphabet():
    print(f"Los Alfabetos registrados hasta el momento son: ")
    # si se deja como lo tenias primero (deivis) de esta forma "print(Alphabet.get_all_alphabet())" va a mostrar 
    # como key (el nombre que es de tipo 'string') y para value al ser de tipo Alphabet(objeto) mostrara la referencia de memoria
    #aqui abajo dos alternativas correctas
    all_alphabets = Alphabet.get_all_alphabets()
    for name in all_alphabets:
        print(f"{name}: {all_alphabets[name].elements}")
    '''
    for name, alphabet_instance in all_alphabets.items():
    print(f"{name}: {alphabet_instance.elements}")
    '''
  
def alphabet_menu():
    
    language_input = input("Digite los conjuntos de alfabeto de la forma A = {f, k, 3} B = {h, 5, h, 2}: ")
    language_input = "A = {f, k, 3} B = {h, 5, h, 2} C = {a, l, 3} D = {h, 5, t, jk}" # esto es mientras se prueba el codigo
    process_set(language_input)
    
    
    while True:
        print("\n    Menú de Operaciones con Alfabetos    ")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Cerradura de estrella")
        print("5. Volver al menú principal")
        choice = input("Selecciona una operación: ")
        
        
        show_all_alphabet()
        
        
        alphabet_names = input("ingrese los nombres de los conjuntos a operar de la forma A B C  o  A, B, C : ")
        alphabet_names = re.findall(r'[^,\s]+', alphabet_names)
       
        result = None
        
        all_alphabets = Alphabet.get_all_alphabets() # en una variable porque no deja iterar sobre el metodo get_all_alphabet, no se el por que
        for name in alphabet_names:
            if name in Alphabet.all_alphabets:
                if result is None:
                    result = Alphabet.get_alphabet(name)
                else:
                    if choice == "1":
                        result = Alphabet(result._union(all_alphabets[name]))
                    elif choice == "2":
                        result = Alphabet(result._intersection(all_alphabets[name]))
                    elif choice == "3":
                        result = Alphabet(result._difference(all_alphabets[name]))
                    elif choice == "4":
                        #corregir, no puede estar aqui
                        num_element = int(input("Ingrese la cantidad de elementos de la cerradura: "))
                        result = result.generate_closure(num_element)
                    elif choice == "5":
                        m.main()
            else:
                print(f"El conjunto {name}, no se encuentra por ende no será procesado")
                
        if result:
            print(f"El resultado es {result.elements}")
        else:
            print("Ningun nombre de alfabeto es valido")