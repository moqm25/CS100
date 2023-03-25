# Name
# CS 100 Section 101
# HW 04, September 19, 2021

#-------Exercise 1 & 2-------
#a.Assigns the values 3, 4 and 5 to the variables a, b and c, respectively.
a,b,c=3,4,5

#b.Write an if statement that prints “OK” if a is less than b
if(a<b):
    print("OK (a<b)")
else:
    print("NOT OK (a<b)")

#c.Write an if statement that prints “OK” if c is less than b
if(c<b):
    print("OK (c<b)")
else:
    print("NOT OK (c<b)")

    #d.Write an if statement that prints “OK” if the sum of a and b is equal to c
if((a+b)==c):
    print("OK ((a+b)==c)")
else:
    print("NOT OK ((a+b)==c)")
    
#e.Write an if statement that prints “OK” if the sum of a squared and b squared equals c squared.
if((a**2 + b**2) == c**2):
    print("OK ((a**2 + b**2) == c**2)")
else:
    print("NOT OK ((a**2 + b**2) == c**2)")

    
#-------Exercise 3-------
color = input("What color? ").lower()
width = int(input("What line width? "))
length = int(input("What line length? "))
shape = input("line, triangle, or square? ").lower()

import turtle
bub=turtle.Turtle()
bub.color(color)
bub.width(width)

if(shape=="line"):
    bub.fd(length)
    
elif(shape=="triangle"):
    bub.fd(length)
    bub.lt(120)
    bub.fd(length)
    bub.lt(120)
    bub.fd(length)
    bub.lt(120)
    
elif(shape=="square"):
    bub.fd(length)
    bub.lt(90)
    bub.fd(length)
    bub.lt(90)
    bub.fd(length)
    bub.lt(90)
    bub.fd(length)
    bub.lt(90)
else:
    "Not sure what shape you chose, good luck next time."


