class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def _hash(self, key):
        
        """
        Hashes a given key and returns the index of the hashed key

        This function takes a string key and returns the index of the hashed key
        using the FNV-1a hash algorithm. The FNV-1a hash is a
        non-cryptographic hash function designed to be fast while maintaining a good
        distribution of hash values.

        params:
            key (str): The string key to be hashed

        returns:
            int: The index of the hashed key
        """
        my_hash = 0
        for letter in key:
            ## ord (ordinal) retrieves the ASCII number for that letter/character 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) ## 23 is a prime number, you could use any prime number instead of 23
        return my_hash
    
    def print_table(self):
        """
        Print the hash table
        
        This function prints out the contents of the hash table
        by iterating over the self.data_map list and printing out
        each index and its corresponding value.
        
        params:
            None
        returns:
            None
        """
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)
    
    def set_item(self, key, value):
        """
        Set an item in the hash table
        using the given key and value
        
        params:
            key: Any (key to be used in the hash table)
            value: Any (value to be stored in the hash table)
        returns:
            None
        """
        index = self._hash(key=key)
        if self.data_map[index] is None: 
            self.data_map[index] = []
        self.data_map[index] += [[key, value]]
    def get_item(self, key):
        """
        Get an item from the hash table using the given key
        
        This function takes a key as a parameter and returns
        the corresponding value from the hash table if it exists.
        If the key does not exist in the hash table, it returns
        None.
        
        params:
            key: Any (key to be used in the hash table)
        returns:
            Any (value associated with the key in the hash table)
        """
        index = self._hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None
    
    def keys(self):
        """
        Returns a list of all keys in the hash table
        
        This function takes no parameters and returns a list of all keys in the hash table.
        
        returns:
            list: A list of all keys in the hash table
        """
        all_keys = []
        for item in self.data_map:
            if item:
                for child in item:
                    all_keys.append(child[0])
        return all_keys 
        

my_hash_table = HashTable()
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)
print(my_hash_table.get_item("lumber"))
print(my_hash_table.keys())


