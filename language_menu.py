from Language import Language
import re
import os
import main as m
import msvcrt as ms

def process_set(language):
    
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    all_sets = re.findall(pattern, language)
    
    for _set in all_sets:
        name = _set[0]  # Nombre del conjunto
        values = re.findall(r'[^,\s]+', _set[1])  # Lista de valores del conjunto
        Language.add_language(name, values)

def show_all_language():
    print(f"Los Alfabetos registrados hasta el momento son: ")
    all_languages = Language.get_all_languages()
    for name in all_languages:
        if all_languages[name].elements:
            print(f"{name}: {all_languages[name].elements}")
    
def ask_name_language():
    language_names = input("\nIngrese los nombres de los lenguajes a operar de la forma L1 L2 L3 o L1, L2, L3: ")
    return re.findall(r'[^,\s]+', language_names)
    
def language_menu():
    
    os.system('cls')
    
    language_input = input("Digite los conjuntos de lenguanjess de la forma L1 = {cocina, pollo, Ingredientes} L2 = {programador, internet, ordenador, python}: ")
    language_input = "L1 = {fear, key, high} L2 = {hook, foot, kigs, 2}  L3 = {alex, daniel, deivis} D = {hello, bye, hi}" # esto es mientras se prueba el codigo
    process_set(language_input)
    
    
    #para este se hace igual que en el menu de alfabeto
    while True:

        os.system('cls')

        print("\n Menú de Operaciones con Lenguajes ")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Concatenación")
        print("5. Potencia")
        print("6. Inversión")
        print("7. Cardinalidad")
        print("8. Volver al menú principal")
        choice = input("Selecciona una operación: ")
        
        os.system('cls')
        
        if choice =="8":
            m.main()
        
        show_all_language()
        
        languages_names = ask_name_language()
        
        all_languages = Language.get_all_languages()
        
        result = None
        
        for name in languages_names:
            if name in all_languages:
                if result is None and choice in ("1", "2", "3", "4"):
                    result = Language.get_language(name)
                elif choice == "1":
                    result = Language(result._union(all_languages[name]))
                elif choice == "2":
                    result = Language(result._intersection(all_languages[name]))
                elif choice == "3":
                    result = Language(result._difference(all_languages[name]))
                elif choice == "4":
                    result = Language(result.concatenation(all_languages[name]))
                elif choice == "5":
                    exponent = int(input("ingrese el numero de veces que desee conectar el lenguaje con si mismo(exponente): "))
                    language = Language.get_language(name)
                    result = language.power(exponent)
                    print(f"La potencia de {name} elevado a {exponent} es {result}")
                elif choice == "6":
                    result = all_languages[name].inverse()
                    print(f"El resultado de invertir {name} es {result}")
                elif choice == "7":
                    print(f"La cardinalidad de {name} es {all_languages[name].cardinality()}")
                    result = all_languages[name].cardinality()
                else:
                    print("opcion no valida")
                    pass
            else:
                print(f'el conjunto {name} no se encuentra por ende no puede ser procesado')
        
        if choice in ("1", "2", "3", "4"):
            if result is None:
                print("ningun nombre coincide con los elementos que hay")
            else:
                print(f'El resultado es {result.elements}')
        
        ms.getch()
        os.system('cls')
            
    
        
            

