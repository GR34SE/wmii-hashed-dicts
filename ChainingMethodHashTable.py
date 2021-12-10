class ChainingMethodHashTable:
    DEFAULT_DICT_SIZE = 10

    def __init__(self, size=DEFAULT_DICT_SIZE):
        self.dict_size = size
        self.dict = [[] for _ in range(self.dict_size)]

    def _get_hash(self, key):
        return hash(key) % self.dict_size

    def insert(self, key, value):
        _hash = self._get_hash(key)
        found = False

        for index, entry in enumerate(self.dict[_hash]):
            if len(entry) and entry[0] == key:
                self.dict[_hash][index] = (key, value)
                found = True
        if not found:
            self.dict[_hash].append((key, value))

    def find(self, key):
        _hash = self._get_hash(key)
        for entry in self.dict[_hash]:
            if entry[0] == key:
                return entry[1]

    def delete(self, key):
        _hash = self._get_hash(key)
        for index, tuple_entry in enumerate(self.dict[_hash]):
            if tuple_entry[0] == key:
                del self.dict[_hash][index]
