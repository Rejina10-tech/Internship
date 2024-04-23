#simple printing and executing
print("Hi, Rejina")

#checking python version in system 
import sys
print(sys.version)

#python indentation 
if 52>12:
    print("52 is greater than 12")
    
if 5>2:
    print(5) 
    
#python varaiables 
a=10
print(a) 
b="Rejina" 
print(b)   

#Comments in python
#this is my comment..this part of the code doesnt run or execute 
# to make easier to understand and readable for others aswell

#This is bascially used for single line comment

"""
For multi lines comments we use this triple quotes
"""
#casting variables

x=str(19)
y=int(19)
z=float(19)
print(x)
print(y)
print(z)

#how to get the type 
x=5
y="Rejina"

print(type(x))
print(type(y))

#case-sensitive
a=10
print(a) #prints 10
 #print(A) #it shows error due to case sensitive

#legal variable names
my_name = "Rejina"
print(my_name)
myname = "Rejina"
_my_name = "Rejina"
myName = "Rejina"
MYNAME = "Rejina"
myname2 = "Rejina"

#multiwords variable name
#camel case
myName="Rejina"
#pasal case
MyName="Rejina"
#Snake case
my_name="Rejina"

#many values to multiple variables
x,y,z="dell","hp","lenovo"
print(x)
print(y)
print(z)


#output variables
x = "my name is Rejina Dahal"
print(x)

x = "Rejina "
y = "is "
z = "Happy"
print(x + y + z)

x = 5
y = "Reju"
print(x, y)

#Global Variables
def myFun():
    print("REJINA ")
myFun()
    
x = "girl"

def myfunc():
  x = "student"
  print("Rejina is " + x)

myfunc()

print("Rejina is " + x)    

#functions
def sum(x, y):
    return x + y
result = sum(3, 5)
print("The sum is", result)

#typeconversion

x=1
y=float(x)
print(y)

#random number
import random

print(random.randrange(1,10))


#strings
a = "Hello, World!"
print(a[1])


for x in "banana":
  print(x)
  
a= "birendra" 
print(len(a)) 

#slicing

x = "Hello, World!"
print(x[1:6])

my_list = [10, 20, 30, 40, 50]
print("Last element using negative index:", my_list[-1])   # Prints: 50
print(" first element using negative index:", my_list[-5])   # Prints: 10

#concatenation
x="Rejina"
y="Dahal"
print(x+" "+y)

#fstring
pi = 3.14159265359

# Using f-string to format a floating-point number
formatted_pi = f"Value of pi: {pi:.2f}"
print(formatted_pi)

print(10 > 9)
