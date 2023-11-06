#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with a while loop along with a try...except 
# block so that the user will keep entering in a number
# until they have entered a value integer value

number = input("Please enter in an integer value: ")
x = True
while x == True:
 try:
  number = int(number)
  x = False
 except:
  print("Invalid input\ntry again")
  number = input("Please enter in an integer value: ")
print(number)
