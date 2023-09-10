from alphabet import Alphabet
from language import Language


def enter_set(sets):
    #aqui ira las expresiones regulares que saparan los conjuntos y nombre y valores
    pass
    

def main():
    while True:
        print("\n   Menú   ")
        print("1. Operaciones con Alfabetos")
        print("2. Operaciones con Lenguajes")
        print("3. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == "1":
            alphabet_menu()
        elif choice == "2":
            language_menu()
        elif choice == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    
def alphabet_menu():
    
    #aqui va un input pidiendo los conjuntos y se llama a la funcion enter_set para procesar la cadena de entrada
    
    while True:
        print("\n    Menú de Operaciones con Alfabetos    ")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Cerradura de estrella")
        print("5. Volver al menú principal")

        choice = input("Selecciona una operación: ")
        #aqui se pide los nombre de los dos conjuntos que se van a operar(dependiendo la opcion de arriba)
        #estos dos conjuntos deben ser verificados si se encuentran en la lista, de no encontrarse dar la opcion de agregarlo
        
        
        #if choice == "1":
            #aqui se llama al metodo enter_set para prosesar la entrada
            #aqui se pone un conjunto se llama el metodo correcto y por argumento se pasa el otro conjunto
            #ejemplo a.union(b)
        #lo mismo para choice == "2" y asi sucesivamente

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


if __name__ == "__main__":
    main()