from set_operations import SetOperations

class Language(SetOperations):
    
    def __init__(self, language):
        super().__init__(language)

    def concatenation(self, other_language):
        concatenated_words = list() #primer cambio
        for word1 in self.elements:
            for word2 in other_language.elements: #segundo cambio
                concatenated_words.append(word1 + word2)
        return concatenated_words
    
    def power(self, exponent):
        if exponent == 0:
        # L^0 = {λ} (conjunto que contiene la cadena vacía)
            return {""}
        elif exponent == 1:
        # L^1 = L (el lenguaje original)
            return self.elements
        else:
            result = self.elements
            for _ in range(exponent-1):
                result = self.concatenation(Language(result))
            return result

    def inverse(self):
        inverse_words = {word[::-1] for word in self.elements}
        return inverse_words

    def cardinality(self):
        return len(self.elements)
    
    
    # Compartidos por todas las clases
    
    # atributo de clase para almacenar todos los lenguajes
    all_languages = {}
    
    # Metodos de clases
    
    @classmethod
    def contains_language(cls, name):
        return name in cls.all_languages
    
    @classmethod
    def add_language(cls, name, element):
        if not cls.contains_language(name):
            cls.all_languages[name] = element
        else:
            choice = input(f"el conjunto {name} ya existe, desea modificarlo (si/no)")
            if choice == "si":
                cls.set_alphabet(name, element)

    @classmethod
    def get_all_languages(cls):
        return cls.all_languages
    
    @classmethod
    def get_language(cls, name):
        if cls.contains_language(name):
            return cls.all_languages[name]
    
    @classmethod
    def set_language(cls, name, elements):
        if cls.contains_languages(name):
            cls.all_languagess[name] = Language(elements)

    @classmethod
    def delete_language(cls, name):
        if cls.contains_languages(name):
            del cls.all_languauges[name]


    
    
    
    
