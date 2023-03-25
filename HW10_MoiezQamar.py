import string

# Name
# CS 100 Section 021
# HW 10, November 12, 2021


'''
--------------------------------

Problem 1
Write a function named initial_letters_count that takes one parameter, word_list — a list of words. 
Create and return a dictionary in which each initial letter of a word in word_list is a key and the corresponding 
value is the number of words in word_list that begin with that letter. 
The keys in the dictionary should be case-sensitive, which means 'a' and 'A' are two different keys.

For example, the following is correct output:
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

print(initial_letters_count(horton))

{'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1}

'''
def initial_letters_count(word_list):
    theDict={}
    for i in word_list:
        if i[0] in theDict:
            theDict[i[0]]+=1
        else:
            theDict[i[0]]=1
    return theDict
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initial_letters_count(horton))

notHorton = ['i', 'Say', 'what', 'I', 'mean', 'YO', 'I', 'mean', 'heelllloooooo', 'I', 'say']
print(initial_letters_count(notHorton))

Fruit = ['apple', 'banana', 'carrot', 'Pineapple', 'Cantaloupe', 'watermelon', 'water', 'manog']
print(initial_letters_count(Fruit))


'''
--------------------------------

Problem 2
Write a function named initial_letters_list that takes one parameter, word_list — a list of words. Create and 
return a dictionary in which each initial letter of a word in word_list is a key and the corresponding value 
is a list of the words in word_list that begin with that letter. There should be no duplicate words in any 
value in the dictionary.
For example, the following is correct output:
forrest = ['My', 'mama', 'always', 'said', 'life', 'is', 'is', 'like', 'a', 'box', 'of', 'chocolates']
print(initial_letters_list(forrest))
{'M': ['My'], 'm': ['mama'], 'a': ['always', 'a'], 's': ['said'], 'l': ['life', 'like'], 
    'i': [is], 'b': ['box'], 'o': ['of'], 'c': ['chocolates']}
'''
def initial_letters_list(word_list):
    theDict={}
    for i in word_list:
        if i[0] in theDict:
            if i in theDict[i[0]]:
                continue
            else:
                theDict[i[0]].append(i)
        else:
            theDict[i[0]]=[i]
    return theDict
forrest = ['My', 'mama', 'always', 'said', 'life', 'is', 'is', 'like', 'a', 'box', 'of', 'chocolates']
print(initial_letters_list(forrest))

notHorton = ['i', 'Say', 'what', 'I', 'mean', 'YO', 'I', 'mean', 'heelllloooooo', 'I', 'say']
print(initial_letters_list(notHorton))

Fruit = ['apple', 'banana', 'carrot', 'Pineapple', 'Cantaloupe', 'watermelon', 'water', 'manogo', 'Pickle']
print(initial_letters_list(Fruit))


'''
--------------------------------

Problem 3
Write a function named group_by_length that takes one parameter, sentence — a string consisting of 
multiple words. The function group_by_length returns a dictionary in which each key is the length of a 
word in sentence and the corresponding value is a list of all distinct words in sentence of that length. Even 
if a word occurs more than once in sentence, it should appear in a value list only once. Treat the text as 
case sensitive (e.g., “Python” and “python” are two different words). Additionally, remove any leading and 
trailing punctuation (but not interior) from each word before processing it further.
For example, the following is correct output:
twister = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
print(group_by_length(twister))
{3: ['How'], 4: ['much', 'wood'], 5: ['would', 'chuck', 'could'], 1: ['a'], 9: ['woodchuck'], 2: ['if']}
'''
def group_by_length(sentence):
    spliter=sentence.split()
    dicti={}
    count=0
    for i in spliter:
        spliter[spliter.index(i)]=spliter[spliter.index(i)].strip(string.punctuation)
    for i in spliter:
        if len(i) not in dicti:
            dicti[len(i)]=[i]
            continue
        else:
            if i in dicti[len(i)]:
                continue
            else:
                dicti[len(i)].append(i)        
    return dicti
twister = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
print(group_by_length(twister))

me = "hello there, My Name is Moiez Qamar and i am a first Student who is a junior!"
print(group_by_length(me))

Fruit = "apple banana carrot Pineapple Cantaloupe watermelon water manogo Pickle"
print(group_by_length(Fruit))

