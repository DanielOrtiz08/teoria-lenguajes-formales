from Language import Language
import re
import os

def process_set(sets):
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'

    all_sets = re.findall(pattern, sets)
    
    processed_sets = {}
    
    for _set in all_sets:
        name = _set[0]  # Nombre del conjunto
        values = re.findall(r'[^,\s]+', _set[1])  # Lista de valores del conjunto
        processed_sets[name] = values
        Language.all_languages[name] = Language(values)
    

def language_menu():
    
    os.system('cls')
    
    language_input = input("Digite los conjuntos de lenguanjess de la forma L1 = {cocina, pollo, Ingredientes} L2 = {programador, internet, ordenador, python}: ")
    language_input = "L1 = {fear, key, high} L2 = {hook, foot, kigs, 2} L3 = {alex, daniel, deivis} D = {hello, bye, hi}" # esto es mientras se prueba el codigo
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

