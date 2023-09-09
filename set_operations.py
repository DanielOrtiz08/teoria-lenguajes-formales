from abc import ABC, abstractmethod

class SetOperations(ABC):

    @abstractmethod
    def union(self, other_set):
        return SetOperations(self.data.union(other_set.data))
    
    @abstractmethod
    def intersection(self, other_set):
        return SetOperations(self.data.intersection(other_set.data))

    @abstractmethod
    def difference(self, other_set):
        return SetOperations(self.data.difference(other_set.data))
