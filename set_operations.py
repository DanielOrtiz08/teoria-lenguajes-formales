from abc import ABC, abstractmethod

class SetOperations(ABC):
    
    @abstractmethod
    def __init__(self, elements):
        self.elements = set(elements)
        
    def _union(self, other_set):
        return self.elements.union(other_set.elements)
    
    def _intersection(self, other_set):
        return self.elements.intersection(other_set.elements)

    def _difference(self, other_set):
        return self.elements.difference(other_set.elements)
