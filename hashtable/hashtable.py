

from fnvhash import fnv1_64


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

    def __repr__(self):
        return f'key is {self.key}, value is {self.value}'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.arr = [None] * capacity
        self.elements = 0
        
        #for i in capacity:
            #self.arr[i] = LinkedList()
        #print(self.arr)
        #choosing FNV-1 for hashing algorithm due to it having fewer collisions
        #and better hash distribution

    def __repr__(self):
        print(f'Hashtable is ->{self.arr}')

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        print(f'Number of slots in current table: {self.capacity}')
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        print(f'Load factor is: {self.elements/self.capacity}')
        return self.elements/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        instring = key.encode()
        #FNV_prime = (2^40) + (2^8) + 0xb3
        # Your code here
        #key = self.key
        #h = key
        #for char in key:
        #    h = h * FNV_prime    
            #h = h "xor octet of data"
        #return h
        #print(fnv1_64(instring))
        return fnv1_64(instring)
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        """
        Looking into each index, if the index is empty, insert a node
        if there is already a node, check the key, if the key matches
        the current value of the key val pair is replaced
        """
        # Your code here
        hash_index = self.hash_index(key)
        #hashed_key = self.fnv1(key)
        node = self.arr[hash_index]
        while node:
            if node.key == key:
                node.value = value
                return
            if node.next:
                node = node.next
            else:
                node.next = HashTableEntry(key, value)
                self.elements += 1
                return
        self.arr[hash_index] = HashTableEntry(key, value)
        self.elements += 1
        
        #if self.arr[hash_index]:
            #node = self.arr[hash_index]
            #if node.key == hashed_key:
                #node.value = value
            #while node.next:
                #if node.key == hashed_key:
                    #node.key = key #not sure if this is needed
                    #node.value = value
                    
                #node = node.next
            #node.next = HashTableEntry(hashed_key,value)
        #else:
            #self.arr[hash_index] = HashTableEntry(hashed_key,value)
            #self.size += 1
        #self.arr[hash_index] = value
        #print(f'my_array{self.arr}')
        
        #if self.arr[hash_index] == None:
            #self.arr[hash_index] = Node(key,value)
        #else:
            #current = self.arr[hash_index]
            #while current is not None:
                
            
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        #hashed_key = self.fnv1(key)
        node = self.arr[hash_index]

        while node:
            if node.key == key:
                node.value = None
                self.elements -= 1
            if node.next:
                node = node.next
            else:
                print(f'No value found with key: {key}')
                return
        # FIX THIS DELETE FUNCTION TOMORROW

        #if self.arr[hash_index]:
            #node = self.arr[hash_index]
            #if node.key == hashed_key:
                #node.value = None
            #while node.next:
                #if node.key == hashed_key:
                    #node.value = None
                #node = node.next

        


        #if self.hash_index(key) is not None:
            #self.arr[hash_index] = None
        #else:
            #print('Key could not be found')
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        """
        to implement the collision version of this, need to access the node
        and compare the key to the first element stored in the node at the 
        hash address
        """
        # Your code here
        hash_index = self.hash_index(key)
        #hashed_key = self.fnv1(key)
        #if self.arr[hash_index].find(key) == key
        #if self.arr[hash_index].length > 1:

            #for element in self.arr[hash_index]:
                #if len(element) == 2 and element[0] == key:
                   # return element[1]
                #else:
                    #return None
        
        #print(self.arr[hash_index].find(key[0]))
        #print (self.arr[hash_index].find(key))
            #print('found')
        
        #return self.arr[hash_index].find(key)

        #if self.arr[hash_index] is not None:
            #return self.arr[hash_index]
        #else:
            #return None
        
        if self.arr[hash_index]:
            node = self.arr[hash_index]
            while node:
                if node.key == key:
                    #print(f'Node key is {node.key}, Node value is {node.value}')
                    return node.value
                node = node.next
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        if we need to double, then we get load factor size, confirm
        then we need to create a new hashtable with the new size
        then we need to go through the old table and pull in the old entries
        and rehash them into the new table

        Implement this.
        """
        # Your code here
        load_factor = self.get_load_factor()

        if load_factor > 0.7:
            newer_capacity = new_capacity
        if load_factor < 0.2:
            newer_capacity = self.capacity // 2
        new_hashtable = HashTable(newer_capacity)    
        for i in self.arr:
            node = i
            while node:
                new_key = node.key
                new_val = node.value
                new_hashtable.put(new_key, new_val)
                node = node.next
        self.arr = new_hashtable.arr
        self.capacity = new_hashtable.capacity
        
        # 
        # A different way down below       
        #new_hashtable = self
        #self = HashTable(new_capacity)
        #for i in new_hashtable.arr:
            #node = i
            #while node:
                #new_key = node.key
                #new_val = node.value
                #self.put(new_key,new_val)
                #node = node.next
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    #Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

     #Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

     #Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


#a = HashTable(8)

#a.put("key-0", "val-0")
#a.put("key-1", "val-1")
#a.put("key-2", "val-2")
#a.put("key-3", "val-3")
#a.put("key-4", "val-4")
#a.put("key-5", "val-5")
#a.put("key-6", "val-6")
#a.put("key-7", "val-7")
#a.put("key-8", "val-8")
#a.put("key-9", "val-9")
#print(a)

#print('key 1')
#a.get('key-1')
#print('key-9')
#a.get('key-9')

#a.put('key-0', 'something else')

##print('new key-0 val')
#a.get('key-0')
#a.delete('key 1')
#print('New key-1')
#a.get('key-1')