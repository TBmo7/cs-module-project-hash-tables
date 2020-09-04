

from fnvhash import fnv1_64

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curStr = ""
        curr = self.head
        while curr is not None:
            curStr += f'{str(curr.value)} ->'
            curr = curr.next
        return curStr

    def insert_at_head(self,node):
        
        node.next = self.head
        self.head = node

    def insert_at_head_or_overwrite(self,node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    def delete(self,value):
        curr = self.head

        if curr.value == value:
            self.head = curr.next
            return curr
        
        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    def find(self,value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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
        self.arr = [LinkedList()] * capacity
        #for i in capacity:
        #    self.arr[i] = LinkedList()
        #print(self.arr)
        #choosing FNV-1 for hashing algorithm due to it having fewer collisions
        #and better hash distribution

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


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
        # Your code here
        hash_index = self.hash_index(key)
        #self.arr[hash_index] = value
        #print(f'my_array{self.arr}')
        self.arr[hash_index].insert_at_head_or_overwrite(Node(value))
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.hash_index(key) is not None:
            self.arr[hash_index] = None
        else:
            print('Key could not be found')
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.arr[hash_index] is not None:
            return self.arr[hash_index]
        else:
            return None
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


a = HashTable(8)
#a.put('today',140)
#b = a.hash_index("line_1")

#print (b)