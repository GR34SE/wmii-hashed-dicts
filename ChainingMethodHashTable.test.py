from ChainingMethodHashTable import ChainingMethodHashTable

if __name__ == '__main__':
    test = ChainingMethodHashTable()
    test.insert("test:key", "test:value")

    print test.find("test:key")
