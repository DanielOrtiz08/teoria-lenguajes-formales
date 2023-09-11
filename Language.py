from set_operations import SetOperations

class Language(SetOperations):
    
    def __init__(self, language):
        super().__init__(language)

    def concatenation(self, other_language):
        concatenated_words = set()
        for word1 in self.elements:
            for word2 in other_language:
                concatenated_words.add(word1 + word2)
        return concatenated_words
    
    def power(self, exponent):
        language = self.elements
        if exponent == 0:
        # L^0 = {λ} (conjunto que contiene la cadena vacía)
            return {""}
        elif exponent == 1:
        # L^1 = L (el lenguaje original)
            return language
        else:
            result = language
            for _ in range(exponent-1):
                result = self.concatenation(result)
            return result

    def inverse(self):
        inverse_words = {word[::-1] for word in self.elements}
        return Language(inverse_words)

    def cardinality(self):
        return len(self.elements)
    
    
    # Compartidos por todas las clases
    
    # atributo de clase para almacenar todos los lenguajes
    all_languages = {}
    
    # Metodos de clases
    @classmethod
    def add_language(cls, name, element):
        if name not in cls.all_languages:
            cls.all_languages[name] = element
        else:
            choice = input(f"el conjunto {name} ya existe, desea modificarlo (si/no)")
            if choice == "si":
                cls.set_alphabet(name, element)

    @classmethod
    def get_all_languages(cls):
        return cls.all_languages
    
    @classmethod
    def get_languages(cls, name):
        if cls.contains_languages(name):
            return cls.all_languages[name]
    
    @classmethod
    def set_languages(cls, name, elements):
        if cls.contains_languages(name):
            cls.all_languagess[name] = Language(elements)

    @classmethod
    def delete_languages(cls, name):
        if cls.contains_languages(name):
            del cls.all_languauges[name]


    
    
    
    
