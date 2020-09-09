def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
        total &= 0xffffffff
    return total

my_array = [None] * 8

#add
def put(key,value):
    hash_index = my_hash(key) % 8 
    my_array[hash_index] = value

#Get a Value
def get(key,value):
    hash_index = my_hash(key) % 8
    print(my_array[hash_index])


#Delete a Value
def delete(key,value):
    hash_index = my_hash(key) % 8
    my_array[hash_index] = None
print(my_array)

put("Hello", "Hello value")
put("World", 'World Value')
put("foo", 'foo value')

print(my_array)

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


a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
ll.insert_at_head_or_overwrite(a)
print(ll)