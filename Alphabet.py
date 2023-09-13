from set_operations import SetOperations
import random
import math
import msvcrt as m

#funcion usada para la cerradura de estrella
# tamaño del conjunto(n), elementos de la cerradura(C)
def calcular_max_k(n, C):
    # Calcula el valor máximo de simbolos +*posible o mas conveniente de k
    k = math.log(C * (n - 1) + n, n) - 1
    k = math.ceil(k) #redondea hacia arriba
    return int(k)  # Convierte k a entero

class Alphabet(SetOperations):
    
    def __init__(self, alphabet):
        super().__init__(alphabet)
    
    def generate_closure(self, num_elements):
        kleene_closure = set()
        len = self.elements.__len__()
        max_k = calcular_max_k(len, num_elements)
        while(num_elements > 0):
            word = ""
            for _ in range(random.randint(1,max_k)):
                word += (random.choice(tuple(self.elements)))
            if word not in kleene_closure:
                kleene_closure.add(word)
                num_elements -= 1
        return kleene_closure
        
    
    # COMPARTIDOS POR TODAS LAS INSTANCIAS
    
    #atributo de clase para almacenar todos los lenguajes
    all_alphabets = {}
    
    #Metodos de clase para operar sobre los lenguajes almacenados
    
    @classmethod
    def contains_alphabet(cls, name):
        return name in cls.all_alphabets
    
    @classmethod
    def add_alphabet(cls, name, elements):
        if not cls.contains_alphabet(name):
            cls.all_alphabets[name] = Alphabet(elements)
        else:
            choice = input(f"el conjunto {name} ya existe, desea modificarlo (si/no)")
            if choice == "si":
                cls.set_alphabet(name, elements)
    
    @classmethod
    def get_all_alphabets(cls):
        return cls.all_alphabets
    
    @classmethod
    def get_alphabet(cls, name):
        if cls.contains_alphabet(name):
            return cls.all_alphabets[name]
    
    @classmethod
    def set_alphabet(cls, name, elements):
        if cls.contains_alphabet(name):
            cls.all_alphabets[name] = Alphabet(elements)

    @classmethod
    def delete_alphabet(cls, name):
        if cls.contains_alphabet(name):
            del cls.all_alphabets[name]
