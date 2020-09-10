import re
def word_count(s):
    # Your code here
    dictionary = dict()
    #words = re.split('\s+',s)
    #x = s.lower()
    #words = x.split()
    x = re.sub("[^0-9a-zA-z']+", ' ', s).rstrip()
    y = x.lower()
    words = y.split(' ')

    for i in words:
        value = 0
        
        if i == '':
            return dictionary
        
        if i in dictionary:
            value = dictionary.get(i)
            value += 1
            update = {i:value}
            dictionary.update(update)
            
        
        else:
            value = 1
            update = {i:value}
            dictionary.update(update)
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))