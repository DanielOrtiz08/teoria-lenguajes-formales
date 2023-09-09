from set_operations import SetOperations

class Language(SetOperations):
    
    def __init__(self, language):
        self.language = set(language)

    def concatenation(self, other_language):
        concatenated_words = {word1 + word2 for word1 in self.language for word2 in other_language}
        return Language(concatenated_words)
    
    def power(self, exponent):
        language = self.language
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
        inverse_words = {word[::-1] for word in self.language.data}
        return Language(inverse_words)

    def cardinality(self):
        return len(self.language.data)


    
    
    
    
