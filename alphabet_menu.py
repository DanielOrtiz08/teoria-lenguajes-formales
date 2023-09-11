from alphabet import Alphabet
import re

def process_set(alphabets):
    
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    all_alphabets = re.findall(pattern, alphabets)
    
    for sets in all_alphabets:
        name = sets[0]  # Nombre del conjunto
        values = re.findall(r'[^,\s]+', sets[1])  # Lista de valores del conjunto
        Alphabet.all_alphabet[name] = Alphabet(values)
        
  
def alphabet_menu():
    
    language_input = input("Digite los conjuntos de alfabeto de la forma A = {f, k, 3} B = {h, 5, h, 2}")
    language_input = "A = {f, k, 3} B = {h, 5, h, 2} C = {a, l, 3} C = {h, 5, t, jk}: "
    process_set(language_input)
    
    
    while True:
        print("\n    Menú de Operaciones con Alfabetos    ")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Cerradura de estrella")
        print("5. Volver al menú principal")
        choice = input("Selecciona una operación: ")
        
        
        print("Alfabetos disponibles para la operación: ")
        for name in Alphabet.all_alphabet:
            print(f"{name}: {Alphabet.all_alphabet[name].elements}")
        alphabet_names = input("ingrese los nombres de los conjuntos a operar de la forma A B C o A, B, C")
        alphabet_names = re.findall(r'[^,\s]+', alphabet_names)
       
       
        result = None

        for name in alphabet_names:
            if name in Alphabet.all_alphabet:
                if result is None:
                    result = Alphabet.all_alphabet[name]
                else:
                    if choice == "1":
                        result = result.union(Alphabet.all_alphabet[name])
                    elif choice == "2":
                        result = result.intersection(Alphabet.all_alphabet[name])
                    elif choice == "3":
                        result = result.difference(Alphabet.all_alphabet[name])
                    elif choice == "4":
                        pass
                    elif choice == "5":
                        break
            else:
                print(f"El conjunto {name}, no se encuentra por ende no será procesado")
                
        if result:
            print(f"El resultado es {result}")
        else:
            print("Ningun nombre de alfabeto es valido")