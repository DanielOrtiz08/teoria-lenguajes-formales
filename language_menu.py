from Language import Language
import re

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
    #para este se hace igual que en el menu de alfabeto
    while True:
        print("\n=== Menú de Operaciones con Lenguajes ===")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Concatenación")
        print("5. Potencia")
        print("6. Inversión")
        print("7. Cardinalidad")
        print("8. Volver al menú principal")

        choice = input("Selecciona una operación: ")

