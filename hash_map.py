# Course: CS261 - Data Structures
# Assignment 5 - Hash Map and Min Heap Implementation (Portfolio Assignment)
#   Part 1 - Hash Map
# Student: Steven Ouk
# Description: Complete the hash map by finishing the provided skeleton code.
#   This hash map uses a hash table of buckets, each containing a linked list of hash links. 
#   Each hash link stores the key-value pair (string and object in this case) 
#   and a pointer to the next link in the list.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        params: None
        returns: None
        Clears the content of the hash map. 
        Does not change underlying hash table capacity.
        """
        self.buckets = DynamicArray()
        for _ in range(self.capacity):
            self.buckets.append(LinkedList())
        self.size = 0

    def get(self, key: str) -> object:
        """
        params: A key (string)
        returns: An object
        Returns the value associated with the given key.
        Returns None if the key is not in the hash map.
        """
        # get index using hash function
        hash_value = self.hash_function(key)
        index = hash_value % self.capacity
        lst = self.buckets.get_at_index(index)
        # if list contains key, return value
        if lst.contains(key):
            node = lst.contains(key)
            return node.value
        # else, return None
        return None

    def put(self, key: str, value: object) -> None:
        """
        params: A key (string), A value (object)
        returns: None
        Updates the key/value pair in the hash map. 
        If a given key already exists, its associated value should be replaced with the new value.
        """
        # get index using hash function
        hash_value = self.hash_function(key)
        index = hash_value % self.capacity
        lst = self.buckets.get_at_index(index)
        # if list contains key, update its value
        if lst.contains(key):
            node = lst.contains(key)
            node.value = value
            return
        # else, insert the key/value pair in the list
        lst.insert(key, value)
        self.size += 1

    def remove(self, key: str) -> None:
        """
        params: A key (string)
        returns: None
        Removes the given key and its associated value from the hash map.
        If a given key is not in the hash map, the method does nothing.
        """
        # get index using hash function
        hash_value = self.hash_function(key)
        index = hash_value % self.capacity
        lst = self.buckets.get_at_index(index)
        if not lst.remove(key):
            return
        self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        params: A key (string)
        returns: A boolean
        Returns True if the given key is in the hash map. Else, return False.
        """
        # get index using hash function
        hash_value = self.hash_function(key)
        index = hash_value % self.capacity
        lst = self.buckets.get_at_index(index)
        if lst.contains(key):
            return True
        return False

    def empty_buckets(self) -> int:
        """
        params: None
        returns: An integer
        Returns a number of empty buckets in the hash table.
        """
        res = 0
        for lst in self.buckets:
            if lst.size == 0:
                res += 1
        return res
            
    def table_load(self) -> float:
        """
        params: None
        returns: A float
        Returns the current hash table load factor.
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        params: A new capacity (integer)
        returns: None
        Changes the capacity of the internal hash table.
        All existing key/value pairs must remain in the new hash map
        and all hash table links must be rehashed.
        If new capacity is less than 1, this method should do nothing.
        """
        if new_capacity < 1:
            return
        # put all key/value pairs into a DynamicArray
        nodes = DynamicArray()
        for lst in self.buckets:
            current = lst.head
            while current:
                nodes.append(current)
                current = current.next
        # initialize new hash table with same size and new capacity
        self.buckets = DynamicArray()
        for _ in range(new_capacity):
            self.buckets.append(LinkedList())
        # iterate through DynamicArray and insert key/value pairs into new hash table
        for node in nodes:
            # get index using hash function
            hash_value = self.hash_function(node.key)
            index = hash_value % new_capacity
            lst = self.buckets.get_at_index(index)
            lst.insert(node.key, node.value)
        self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        """
        params: None
        returns: A DynamicArray
        Returns a DynamicArray that contains all keys stored in the hash map.
        The order of the keys in the DynamicArray does not matter.
        """
        res = DynamicArray()
        for lst in self.buckets:
            current = lst.head
            while current:
                res.append(current.key)
                current = current.next
        return res


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
