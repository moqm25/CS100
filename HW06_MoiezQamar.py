# Name
# CS 100 Section 029
# HW 06, October 19, 2021


#Write a function named has_final_letter that takes two parameters:
#   1. str_list, a list of non-empty strings
#   2. letters, a string of upper and/or lower case letters
# The function has_final_letter should create and return a list of all the strings in 
#str_list that end with a letter in letters.

#exercise 1:

def has_final_letter(str_list, letters):
    has_the_letter = []
    for word in str_list:
        if word[-1] in letters:
            has_the_letter.append(word)
    return has_the_letter

word1 = 'Hello'; word2 = 'there'
word3 = 'How do you do'
word4 = 'pizza'
word5 = 'NJIT'
wordy_list = [word1, word2, word3, word4]
potatoWord = 'potato'
potatoeWord = 'pOTaTOe'
notPotatoWord = 'ApplE'
#Call 1.1:
print("1. run 1) ", has_final_letter(wordy_list, potatoWord))

#Call 1.2:
print("1. run 2) ", has_final_letter(wordy_list, potatoeWord))

#Call 1.3:
print("1. run 3) ", has_final_letter(wordy_list, notPotatoWord))


def is_divisible(max_int, two_ints):
    uno = two_ints[0]
    dos = two_ints[1]
    not_a_tuple = []
    for x in range(1,max_int):
        if ((x%uno==0)and(x%dos==0)):
            not_a_tuple.append(x)
    return not_a_tuple      
#Call 2.1:
print("2. run 1) ", is_divisible(5, (2,3)))

#Call 2.2:
print("2. run 2) ", is_divisible(20, (4,2)))

#Call 2.3:
print("2. run 3) ", is_divisible(60, (4,5)))



            