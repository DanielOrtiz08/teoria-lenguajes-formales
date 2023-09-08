class SetOperations:
    def __init__(self, data):
        self.data = set(data)

    def union(self, other_set):
        return SetOperations(self.data.union(other_set.data))

    def difference(self, other_set):
        return SetOperations(self.data.difference(other_set.data))

    def intersection(self, other_set):
        return SetOperations(self.data.intersection(other_set.data))

    def cardinality(self):
        return len(self.data)