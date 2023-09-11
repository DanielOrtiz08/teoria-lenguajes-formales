from set_operations import SetOperations
import random

class Alphabet(SetOperations):
    
    def __init__(self, alphabet):
        super().__init__(alphabet)
    
    def generate_closure(self, num_element):
        random_words = [''.join(random.choice(self.set_operations.data) for _ in range(5)) for _ in range(num_element)]
        return random_words
    
    
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
            choice = input("el conjunto ya existe, desea modificarlo (si/no)")
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
