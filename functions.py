# function definition

def cylinder_volume(height, radius):
    pi = 3.14159
    return height  *pi*  radius ** 2
print(cylinder_volume(10,3)) #prints 282.7431


#default argument

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height  *pi*  radius ** 2
print(cylinder_volume(10)) #prints 785.3975


#variable scope
 #the parts of a program that a variable can be 
 #referenced or used from 
 
def some_function():
    word = "hello"
 
#print(word) #not defined error


def some_function():
    word = "hello"
 
def another_function():
    word = "goodbye"
    
    print(word)

word = "hello"

def some_function():
    print(word)
    
    
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()