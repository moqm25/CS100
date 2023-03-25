# Name
# CS 100 Section 029
# HW 11, December 06, 2021

'''
Write a class definition line and an appropriate one line docstring for the class Dog. Write an __init__ 
method for the class Dog that gives each dog its own name and breed. Test this on a successful creation of 
a Dog object.
>>> sugar = Dog('Sugar', 'border collie')
>>> sugar.name
'Sugar'
>>> sugar.breed
'border collie'
'''

class Dog:
    '''This class creates a Dog Object'''
    species = 'canis familiaris'
    def __init__(self, name, breed, tricks=[]):
        self.name = name
        self.breed = breed
        self.tricks = tricks
        
    def teach(self, trickaDoodle):
        if trickaDoodle in self.tricks:
            print("Begone, trick has already been learnt :P")
        else:
            self.tricks.append(trickaDoodle)
            print("This trick has been learnt :)")
            
    def knows(self, trickarooo):
        if trickarooo in self.tricks:
            print("{} is in {}\'s list of tricks".format(trickarooo,self.name))
            return True
        else:
            print("{} is not in {}\'s list of tricks".format(trickarooo,self.name))
            return False

#problem 1 testing
print("problem 1 testing:")
sugar1 = Dog('Sugar', 'border collie')
print(sugar1.name)
print(sugar1.breed)

#problem 2 testing
print("\nproblem 2 testing:")
sugar2 = Dog('Sugarooooooo', 'tiny', ['jump', 'fly', 'laser eyes', 'sleep'])
print(sugar2.tricks)
sugar3 = Dog('Bug', 'Wolf')
print(sugar3.tricks)

#problem 3 testing
print("\nproblem 3 testing:")
sugar2.teach('kick')
print(sugar2.tricks)
sugar2.teach('sleep')
print(sugar2.tricks)
sugar3.teach('fly')
print(sugar2.tricks)
sugar3.teach('drive')
print(sugar3.tricks)

#problem 4 testing
print("\nproblem 4 testing:")
print(sugar2.knows('juggling'))
print(sugar3.knows('drive'))

#problem 5 testing
print("\nproblem 5 testing:")
print(sugar1.species)
print(sugar2.species)
print(sugar3.species)

