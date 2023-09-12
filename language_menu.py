from Language import Language
import re
import os
import main as m

def process_set(language):
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'

    all_sets = re.findall(pattern, language)
    
    for _set in all_sets:
        name = _set[0]  # Nombre del conjunto
        values = re.findall(r'[^,\s]+', _set[1])  # Lista de valores del conjunto
        Language.all_languages[name] = Language(values)

def show_all_language():
    print(f"Los Alfabetos registrados hasta el momento son: ")
    all_languages = Language.get_all_languages()
    for name in all_languages:
        print(f"{name}: {all_languages[name].elements}")
    
def ask_name_language(choice):
    if choice not in ("5"):
        language_names = input("Ingrese los nombres de los lenguajes a operar de la forma A B C o A, B, C: ")
        return re.findall(r'[^,\s]+', language_names)
    else:
        return input("Ingrese el nombre del conjunto a operar: ")
    
def language_menu():
    
    os.system('cls')
    
    language_input = input("Digite los conjuntos de lenguanjess de la forma L1 = {cocina, pollo, Ingredientes} L2 = {programador, internet, ordenador, python}: ")
    language_input = "L1 = {fear, key, high} L2 = {hook, foot, kigs, 2}  L3 = {alex, daniel, deivis} D = {hello, bye, hi}" # esto es mientras se prueba el codigo
    process_set(language_input)
    
    
    #para este se hace igual que en el menu de alfabeto
    while True:
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
        
        if choice =="8":
            m.main()
        
        show_all_language()
        
        languages_names = ask_name_language(choice)
        
        all_languages = Language.get_all_languages()
        
        result = None
        
        for name in languages_names:
            if name in all_languages:
                if result is None and choice != "5":
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
                    exponent = int(input("ingrese el numero de veces que desee conectar el lenguaje con si mmismo(exponente)"))
                    language = Language.get_language(name)
                    power = language.power(exponent)
                    result = Language(power)
            else:
                print(f'el conjunto {name} no se encuentra por ende no puede ser procesado')
        
        if result:
            print(f'El resultado es {result.elements}')
        else:
            print("ningun nombre coincide con los elementos que hay")
    
        
            

