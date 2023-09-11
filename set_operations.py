from abc import ABC, abstractmethod

class SetOperations(ABC):
    
    @abstractmethod
    def _init_(self, elements):
        self.elements = set(elements)
        
    def union(self, other_set):
        return self.elements.union(other_set.elements)
    
    def intersection(self, other_set):
        return self.elements.intersection(other_set.elements)

    def difference(self, other_set):
        return self.elements.difference(other_set.elements)
