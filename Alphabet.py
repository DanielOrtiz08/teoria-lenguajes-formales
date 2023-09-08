from set_operations import SetOperations
import random

class Alphabet():
    def _init_(self, alphabet):
        self.set_operations = SetOperations(alphabet)
    
    def generate_closure(self, num_element):
        random_words = [''.join(random.choice(self.symbols) for _ in range(5)) for _ in range(num_element)]
        return random_words