class Entry:
    def __init__(self, _hash, key, value):
        self.hash = _hash
        self.key = key
        self.value = value


class Deleted:
    pass


class Empty:
    pass


class OpenAddressingHashTable:
    DEFAULT_DICT_SIZE = 10
    MAX_LOAD_FACTOR = 0.66
    MIN_LOAD_FACTOR = 0.33

    def __init__(self):
        self.dict = [Empty] * self.DEFAULT_DICT_SIZE
        self.dict_size = len(self.dict)  # reset on each resize
        self.inserted_amount = 0
        self.deleted_amount = 0

    def _resize_dict(self):
        print "resize dict"
        current_dict = self.dict
        current_dict_size = self.inserted_amount

        self.dict_size = int(current_dict_size // self.MIN_LOAD_FACTOR)
        self.dict = [Empty] * self.dict_size
        self.inserted_amount = 0
        self.deleted_amount = 0

        for entry in current_dict:
            if entry is not Empty and entry is not Deleted:
                self.insert(entry.key, entry.value)

    def _get_entry_and_index(self, key):
        key_hash = self._get_hash(key)

        for offset in range(self.dict_size):
            index = (key_hash + offset) % self.dict_size
            entry_candidate = self.dict[index]

            if entry_candidate is Deleted:
                raise "Entry with given key has been deleted"
            elif entry_candidate is Empty or entry_candidate.hash == key_hash and entry_candidate.key == key:
                return entry_candidate, index
        else:
            raise "Entry with given key does not exist in dictionary"

    def _get_hash(self, key):
        return hash(key)

    def insert(self, key, value):
        entry, index = self._get_entry_and_index(key)
        self.dict[index] = Entry(self._get_hash(key), key, value)

        if entry is Empty:
            self.inserted_amount += 1
        if (self.deleted_amount + self.inserted_amount) / self.dict_size > self.MAX_LOAD_FACTOR:
            self._resize_dict()

    def find(self, key):
        entry, _ = self._get_entry_and_index(key)

        if entry is Empty:
            print "entry is none", entry
            return None
        else:
            return entry.value

    def delete(self, key):
        entry, index = self._get_entry_and_index(key)

        if entry is Empty:
            return None
        else:
            self.dict[index] = Deleted
            self.inserted_amount -= 1
            self.deleted_amount += 1
