from OpenAddressingHashTable import OpenAddressingHashTable

if __name__ == '__main__':
    test = OpenAddressingHashTable()
    test.insert("test:key", "test:value")

    print test.find("test:key")
