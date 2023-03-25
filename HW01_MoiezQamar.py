#-------Exercise 5A-------
# Name
# CS 100 Section 101
# HW 01, September 03, 2021

#-------Exercise 5B-------
age=18
height=70 #inches
siblings=2

#-------Exercise 5C-------
gasPrice=3.19
miles=45.8 #to campus for me
shoeSize=9.5

#-------Exercise 5D-------
favoriteActor="Tom Holland"
firstName="Bob"
lastName="Sponge"

#-------Exercise 1.1-------
#  1. You are given a SyntaxError stating: "SyntaxError: unexpected EOF while parsing". 
#
#  2. If you forget the closing quotation mark, the closing parentheses is considered to be a part of the string and the string does not end, giving a syntaxerror. If you forget both quotes, it considers the supposed string as a variable and will give a NameError that the name is not defined.
#
#  3. If you put a + before a number (2++2 or +2+2), there is no problem, it simply solves the equation.
#
#  4. If you include leading zeros, you get a syntax error which says 'SyntaxError: invalid token'. Neither '09' or '011' work.
#
#  5. If you have two values without an operator between them, you get a SyntaxError saying that it is an invalid syntax.

#-------Exercise 2.1-------

#  1. '42 = n' is not legal because a variable name cannot start with a digit so this results in a SyntaxError stating: "SyntaxError: can't assign to literal".

#  2. 'x = y = 1' is legal, it assigns the value of 1 to both x and y.

#  3. If you include a semicolon at the end of the statement, there is no error, it is legal.

#  4. If you include a period at the end of the statement, you get a SyntaxError, stating "SyntaxError: invalid syntax", meaning that a period is not legal.

#  5. If you try to multiply x and y together like 'xy', you get a name error because Python sees xy as a single variable name, rather than two seperate.

#-------Exercise 1.2-------
#  1. 
minutes=42
seconds=42
totalSeconds= minutes*60 + seconds
print("\n(1.2.1)  There are", totalSeconds, "seconds in",minutes,"minutes","and",seconds,"seconds")
#  2. 
km2mi=1.61
km=10
mi=km/1.61
print("\n(1.2.2) ",km,"km is equal to",round(mi,4),"mi")

#  3. 
#ORIGINAL PROCESS FOR 1.2.3:-----------------------------------
#totalMinutes=minutes+seconds/60
#mimin=mi/totalMinutes
#print("\n(1.2.3)  average pace=",round(mimin,4),"mi/min")
#misec=mi/totalSeconds
#print("         average pace=",round(misec,4),"mi/sec")
#mihr=mi/(totalMinutes*60)
#print("         average pace=",round(totalMinutes,4),"mi/hr")
#--------------------------------------------------------------

#REWRITTEN PROCESS FOR 1.2.3:----------------------------------
minuteS=42
secondS=42
totalMinuteS=minuteS+secondS/60
kM=10
mI=kM/1.61
miMin=mI/totalMinuteS
print("\n(1.2.3)  average pace=",round(miMin,4),"mi/min")
totalSecondS=minuteS*60+secondS
miSec=mi/totalSecondS
print("         average pace=",round(miSec,4),"mi/sec")
mihr=mI/(totalMinuteS/60)
print("         average pace=",round(mihr,4),"mi/hr")
#     Mistake was in this line^ used the incorrect variable
#--------------------------------------------------------------


#-------Exercise 2.2.1-------
#  1. 
#ORIGINAL PROCESS FOR 2.2.1:-----------------------------------
import math
radius=5
volume=((4/3)*(math.pi)*(radius**5))
print("\n(2.2.1)  The volume is:",round(volume,3))
#--------------------------------------------------------------
#REWRITTEN PROCESS FOR 2.2.1:----------------------------------
import math
radius=5
volume=((4/3)*(math.pi)*(radius**3))
#     Mistake was in this line^ raised the radius to the wrong power
print("\n(2.2.1)  The volume is:",round(volume,3))
#--------------------------------------------------------------


#  2.
price=24.95
discount=.40
afterDiscount=price-price*discount
copies=60
cost1=afterDiscount*copies
firstcopy=3
additional=.75
cost2=3+additional*(copies-1)
total=cost1+cost2
print("\n(2.2.2)  The total price is $"+str(round(total,2)))
#  3.
timeLeftSecs=(6*60*60)+(52*60)
easy2secs=(8*60+15)*2
tempo2secs=(7*60+12)*3
timeAfter=timeLeftSecs+easy2secs+tempo2secs
hr=timeAfter//3600
minutes=int((timeAfter%3600)/60)
print("\n(2.2.3)  The time you get home for breakfast is:",str(hr)+":"+str(minutes),"AM")

