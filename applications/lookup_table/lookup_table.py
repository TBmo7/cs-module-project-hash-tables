# Your code here
#import sys
#sys.path.append("./hashtable")
#print(f'system{sys.path}')
#from hashtable import HashTable, HashTableEntry 

import math
import random

ht = dict() 

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.

    Need to cache already solved instances of the two variables x and y
    once something has been solved, store in hash table with x and y as the key
    and v as the value

    hash table needs to be 50000-ish
    """
    # Your code here
    key = x,y
    
    if ht.get(key) is not None:
        return ht.get(key)
    else:
        value = slowfun_too_slow(x,y)
        htupdate = {key:value}
        ht.update(htupdate)

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
