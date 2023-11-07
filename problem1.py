#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import math
import os
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")


at = True
bt = True
ct = True
while at == True:
 a = input("a: ")
 try:
  a = int(a)
  at = False
 except:
  print("invalid input for a\nEnter a new value")
while bt == True:
 b = input("b: ")
 try:
  b = int(b)
  bt = False
 except:
  print("invalid input for b\nEnter a new value")
while ct == True:
 c = input("c: ")
 try:
  c = int(c)
  ct = False
 except:
  print("invalid input for c\nEnter a new value")

try:
 answer = ((0.5**(b*2-(4*a*c)))-b)/(2*a)
 answer = round(answer,2)
except:
  answer = "No Answer"
print(answer)