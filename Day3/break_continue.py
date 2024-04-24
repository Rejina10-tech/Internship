
#the loop stops when i reaches 3 
# because of the break statement.

for i in range(5):
    if i == 3:
        break
    print(i)  #prints 0 1 2
    
    
 #when i equals 2, the continue statement
 # is executed, so the print(i) statement is skipped for that 
 # iteration, but the loop continues 
 # to execute for the next values of i.   
    
for i in range(5):
    if i == 2:
        continue
    print(i) #prints 0 1 3 4

# ZIP returns an iterator that combines multiple
# iterables into one sequence of tuples
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
    
    
 #prints as:   
#a: 1
#b: 2
#c: 3


#enumerate
#s a built in function that returns an iterator of tuples 
# containing indices and values of a list

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
    
#prints 
#0 a
#1 b
#2 c
#3 d
#4 e