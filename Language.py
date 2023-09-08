from set_operations import SetOperations

class Language():
    def __init__(self, language):
        self.language = set(language)

    def concatenation(self, other_language):
        concatenated_words = {word1 + word2 for word1 in self.words for word2 in other_language.words}
        return Language(concatenated_words)
    
    def power(self, exponent):
        pass

    def inverse(self):
        inverse_words = {word[::-1] for word in self.words}
        return Language(inverse_words)



    
    
    
