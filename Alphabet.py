from set_operations import SetOperations
import random

class Alphabet(SetOperations):
    
    def _init_(self, alphabet):
       super().__init__(alphabet)
    
    def generate_closure(self, num_element):
        random_words = [''.join(random.choice(self.set_operations.data) for _ in range(5)) for _ in range(num_element)]
        return random_words
    
    all_alphabet = {}

    @classmethod
    def get_all_alphabet(cls):
        return cls.all_alphabet

    
