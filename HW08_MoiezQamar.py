# Name
#CS 100 Section 021
#HW 08, November 5, 2021

'''
Problem 1:
'''
def two_words(length, first_letter):
    twowords=[]
    while True:
        word = input("Enter a {}-letter word please: ".format(length))
        if len(word)==length:
            twowords.append(word)
            break
    while True:
        word = input("Enter a word that starts with {}: ".format(first_letter))
        if word[0].lower()==first_letter.lower():
            twowords.append(word)
            break
    return twowords


'''
Problem 2:
'''
def two_words(length, first_letter):
    twowords=[]
    rando=True
    while rando==True:
        word = input("Enter a {}-letter word please: ".format(length))
        if len(word)==length:
            twowords.append(word)
            rando=False
    while rando==False:
        word = input("Enter a word that starts with {}: ".format(first_letter))
        if word[0].lower()==first_letter.lower():
            twowords.append(word)
            rando=True
    return twowords

print(two_words(4,'h'))


'''
Problem 3:
'''

def enter_new_password():
    issue1="The password entered does not have 8-15 characters"
    issue2="The password entered does not include 1 digit"
    ib1=ib2=False
    while ((ib1==False) or (ib2==False)):
        wordpass = input("Kindly enter your password(it should be 8-15 characters and at least 1 digit):")
        ib1=ib2=False
        if ((len(wordpass)>=8) and (len(wordpass)<=15)):
            ib1=True
        else:
            print(issue1)
        for x in wordpass:
            if x.isdigit():
                ib2=True 
                
        if ib2==False:
            print(issue2)
    print("Congrats, your password is between 8-15 characters and contains at least 1 digit!")
    
enter_new_password()



import random


'''
Problem 4:
'''
def guess():
    rando=random.randint(0,50)
    counter=5
    while counter>0:
        number=int(input("\nEnter a number from 0-50: "))
        if number==rando:
            print("Congrats, you guessed the correct number!")
            counter=-1
            continue
        elif ((number!=rando) and (counter==1)):
            print("Nice try, you are out of attempts. The correct answer was {}".format(rando))
            counter-=1
        elif (number>rando):
            print("That guess was too high, try again:")
            counter-=1
        elif (number<rando):
            print("That guess was too low, try again:")
            counter-=1 