# Your code here
expensivedict = dict()

def expensive_seq(x, y, z):
    # Your code here
    key = x,y,z
    if expensivedict.get(key) is not None:
        return expensivedict.get(key)
    if x <= 0: 
       value =  y + z
    if x >  0: 
        value = expensive_seq(x-1,y+1,z) +  expensive_seq(x-2,y+2,z*2) +  expensive_seq(x-3,y+3,z*3)
        update = {key:value}
        expensivedict.update(update)
    return value

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
