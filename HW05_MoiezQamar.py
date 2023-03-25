# Name
# CS 100 Section 029
# HW 05, September 24, 2021

#-------Exercise 1-------
# Create a list named months containing each month of the year as a string. 
# Write a for loop that iterates over the elements of months and prints out
# each one that begins with letter 'J', one month per line.

print("Exercise 1:")
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    if month[0]=="J":
        print(month)
    
print("\n")

#-------Exercise 2-------
# Write a for loop that iterates over every integer from 0 through 99, 
# inclusive, and prints out all of the numbers that are divisible by both 2 and 5.
print("Exercise 2:")
for x in range(0,100):
    if ((x%2)==0) and ((x%5)==0):
        print(x, end=" ")

print("\n")

#-------Exercise 3-------
print("Exercise 3:")
horton = "A person's a person, no matter how small."    
vowels = "aeiouAEIOU"
for letter in horton:
    if letter in vowels:
        print(letter, end=" ")




