# Name
# CS 100 Section 101
# HW 03, September 17, 2021

#-------Exercise 1-------
#uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon, each with side length 100.

import turtle
bub=turtle.Turtle()

bub.lt(180)
bub.penup()
bub.fd(200)
bub.lt(180)
#triangle:
bub.pendown()
bub.fd(100)
bub.lt(120)
bub.fd(100)
bub.lt(120)
bub.fd(100)

bub.lt(120)
bub.penup()
bub.fd(200)

#square:
bub.pendown()
bub.fd(100)
bub.lt(90)
bub.fd(100)
bub.lt(90)
bub.fd(100)
bub.lt(90)
bub.fd(100)
bub.lt(90)

bub.penup()
bub.fd(250)

#pentagon:
bub.pendown()
bub.fd(100)
bub.lt(72)
bub.fd(100)
bub.lt(72)
bub.fd(100)
bub.lt(72)
bub.fd(100)
bub.lt(72)
bub.fd(100)
bub.lt(72)



#-------Exercise 2-------
#uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.
bub.penup()
bub.lt(180)
bub.fd(200)
#---
bub.lt(90)
bub.fd(150)
bub.lt(90)
#---
#bub.rt(180)
bub.pendown()
bub.circle(200)

bub.penup()
bub.lt(90)
bub.fd(50)
bub.rt(90)

bub.pendown()
bub.circle(150)

bub.penup()
bub.lt(90)
bub.fd(50)
bub.rt(90)
bub.pendown()
bub.circle(100)

bub.penup()
bub.lt(90)
bub.fd(50)
bub.rt(90)
bub.pendown()
bub.circle(50)



#-------Exercise 3-------
#Write code that uses the Python math module to compute and print out the values of:
import math 
    #100!
print("Exercise 2) \na)\t100! =",math.factorial(100))
    #the log (base 2) of 1,000,000
print("\n\nb)\tthe log (base 2) of 1,000,000 =",math.log2(1000000))

    #the greatest common divisor of 63 and 49
print("\n\nc)\tthe greatest common divisor of 63 and 49 =",math.gcd(63,49))
    

