# Your code here
import re
with open("robin.txt") as f:
    words = f.read()

x = re.sub("[^0-9a-zA-z']+", ' ', words).rstrip()
y = x.lower()
words2 = y.split(' ')
word_holder = {}

"""
after the regex > put in key value pair into dict
word is the key > number of occurrances is value
when getting out put get each item in the dict 
"""
for element in words2:
    if element in word_holder:
        #if the word is found in the holder, increment
        word_holder[element] += 1
    else:
        word_holder[element] = 1

sorted_elements = sorted(sorted(word_holder.items(), key = lambda x: x[0]), key = lambda x : x[1], reverse = True)
#use nested sorteds,using both the count and alphabetized, but reversing only the count
#print(sorted_elements)

#sorted_elements = word_holder.items()
for element in sorted_elements:
    out_hash = element[1]
    #print(f'\n {element[0]}  {'#' * out_hash}')
    print(f'{element[0]}  ', '#'* out_hash) 


 
