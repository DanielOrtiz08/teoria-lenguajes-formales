from Alphabet import Alphabet
import main as m
import re
import os

def process_set(alphabets):
    
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    all_alphabets = re.findall(pattern, alphabets)
    
    for sets in all_alphabets:
        name = sets[0]  # Nombre del conjunto
        values = re.findall(r'[^,\s]+', sets[1])  # Lista de valores del conjunto
        Alphabet.add_alphabet(name, values)
        
        
def show_all_alphabet():
    print(f"Los Alfabetos registrados hasta el momento son: ")
    all_alphabets = Alphabet.get_all_alphabets()
    for name in all_alphabets:
        print(f"{name}: {all_alphabets[name].elements}")
    '''
    for name, alphabet_instance in all_alphabets.items():
    print(f"{name}: {alphabet_instance.elements}")
    '''

def ask_name_alphabet(choise):
    if choise not in ("4"):
        alphabet_names = input("Ingrese los nombres de los conjuntos a operar de la forma A B C o A, B, C: ")
        return re.findall(r'[^,\s]+', alphabet_names)
    else:
        return input("Ingrese el nombre del conjunto a operar para la cerradura de estrella: ")

def alphabet_menu():
    
    os.system('cls')
    
    alphabet_input = input("Digite los conjuntos de alfabeto de la forma A = {f, k, 3} B = {h, 5, h, 2}: ")
    alphabet_input = "A = {f, k, 3} B = {h, 5, h, 2} C = {a, l, 3} D = {h, 5, t, jk}" # esto es mientras se prueba el codigo
    process_set(alphabet_input)
    
    
    while True:

        print("\n    Menú de Operaciones con Alfabetos    ")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Cerradura de estrella")
        print("5. Volver al menú principal")
        choice = input("Selecciona una operación: ")
        
        if choice == "5":
            os.system('cls')
            m.main()
        
        show_all_alphabet()
        
        alphabet_names = ask_name_alphabet(choice)
       
        result = None
        
        all_alphabets = Alphabet.get_all_alphabets() # en una variable porque no deja iterar sobre el metodo get_all_alphabet, no se el por que
        for name in alphabet_names:
            if name in Alphabet.all_alphabets:
                if result is None and choice != "4":
                    result = Alphabet.get_alphabet(name) #tercer cambio,
                elif choice == "1":
                    result = Alphabet(result._union(all_alphabets[name]))
                elif choice == "2":
                    result = Alphabet(result._intersection(all_alphabets[name]))
                elif choice == "3":
                    result = Alphabet(result._difference(all_alphabets[name]))
                elif choice == "4":
                    num_elements = int(input(f"Ingrese la cantidad de elementos para la cerradura estrella del conjunto {name}: "))
                    alphabet = Alphabet.get_alphabet(name)
                    clousure = alphabet.generate_closure(num_elements)
                    result = Alphabet(clousure)
                    break
            else:
                print(f"El conjunto {name}, no se encuentra por ende no será procesado")
                
        if result:
            print(f"El resultado es {result.elements}")
        else:
            print("Ningun nombre de alfabeto es valido")