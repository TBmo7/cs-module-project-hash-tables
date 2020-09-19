# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

"""
split the words > go over the letters in each word > attribute the key to frequency
use key to make cipher  > apply cipher
"""

import re
with open("ciphertext.txt") as f:
    words = f.read()

#x = re.sub("[^0-9a-zA-z']+", ' ', words).rstrip()
#y = x.lower()
words2 = words.split(' ')
letter_holder = {}
frequency_table = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
key_dict = {}
#key dict will be what links the input letter with the proper one
"""
loop through each word looking for letters > if the letter isn't found add it
if it is found update the value
"""
def frequency_analyzer(words_here):
    for element in words_here:
        for letter in element:
            if letter in letter_holder:
                letter_holder[letter] += 1
            else letter_holder[letter] = 0

def key_maker(word_input):
    sorted_elements = sorted(word_input.items(), key = lambda x : x[1], reverse = True)