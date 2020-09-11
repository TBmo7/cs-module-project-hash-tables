import random
from os import getcwd
print(getcwd())
# Read in all the words in one go
#"C:\Users\tbmoo\Desktop\WebPT13\cs-module-project-hash-tables\applications\markov\input.txt"
with open("input.txt") as f:
    words = f.read()
#f = open("input.txt", "r")
#words = f.read()
"""
Need to take all the words in and split them into 

Words

Starts

Stops

"""
word_list = words.split()

starts = {}
stops = {}
continue_words = {}



# TODO: analyze which words can follow other words
# Your code here
def canfollow(s):
    """
    will check the input string to see if it is a start or a stop word
    if it is a start word, skip it, if it is a stop word, signal an end True or something
    else, return the word and the continue operation signal 0 or false

    """
    #stop_word = False
    last = len(s) - 1
    punctuation = {".":".","?":"?","!":"!"}#this is a list of ! . ? or "
    
    #Below, check to see if the input word exists in tables already
    if s in stops:
        #stop_word = True
        #return s
        return
    if s in continue_words:
        return
    if s in starts:
        return
    
    if s[last] in punctuation or s[last-1] in punctuation:
        #stop_word = True
        update = {s:s}
        stops.update(update)
        return
        #return s 
    if s[0].isupper() or (s[0] == '"' and s[1].isupper()):
        #this is the condition for start words, will use this down below, this function doesn't care about these words
        update = {s:s}
        starts.update(update)
    else:
        update = {s:s}
        continue_words.update(update)
        #return s



# TODO: construct 5 random sentences
# Your code here
def constructor(s,num):
    """
    takes input s and then runs through
    FIRST - looks for a start word -> begins with uppercase OR quote mark and then UPPERCASE
    take in the whole list, and a number for number of sentences
    loop through and throw everthing into can follow to document
    keep going through until a start word
    once a start word has been found
    """
    constructed = 0
    #started = False
    #stopped = False
    for word in s:
        canfollow(word)
    while constructed < num:

        word = random.choice(list(starts.values()))
        print(word, end = " ")
        stopped = False
        counter = 0
        while stopped is False:
                
                randnum = random.choice(range(0,100))
                #randomize list that the program chooses from, but
                #make the sentences longer, with a guranteed 100 word max length-ish
                if randnum > counter: 
                    continue_word = random.choice(list(continue_words.values()))
                    print(continue_word, end = " ")
                    counter += 1
                else:
                    end_word = random.choice(list(stops.values()))
                    print(end_word, end = " " )
                    constructed += 1
                    stopped = True
    
constructor(word_list,5)


   
