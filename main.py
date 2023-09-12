import alphabet_menu as am
import language_menu as lm
    
def main():
    while True:
        print("\n   Menú   ")
        print("1. Operaciones con Alfabetos")
        print("2. Operaciones con Lenguajes")
        print("3. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == "1":
            am.alphabet_menu()
        elif choice == "2":
            lm.language_menu()
        elif choice == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
  
if __name__ == "__main__":
    main()