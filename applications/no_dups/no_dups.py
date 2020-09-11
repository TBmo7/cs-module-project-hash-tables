def no_dups(s):
    # Your code here
    """
    for no dups, take the input string, split into words on spaces
    take each word and store as a key with value True
    for each word check the table to see if the value exists, if it does exist
    skip it, if it doesn't store it
    """
    word_storage = {}
    string = s.split()
    out_str = " "

    for word in string:
        if word in word_storage:
            pass
        else:
            update = {word:True}
            word_storage.update(update)
    #for key in word_storage.keys():
        #out_str += key
    
    
    return out_str.join(word_storage)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))