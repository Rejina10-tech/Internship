#list is  data structure in python that is mutable and ordered

months = ['January', 'February', 'March',
          'April', 'May', 'June', 'July', 'August', 
          'September', 'October', 'November', 'December']

print(months[2]) #prints march
print(months[-1]) #prints december
# print(months[29]) #prints IndexError: list index out of range

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0]) #prints 1

#Slice and Dice with Lists
print(list_of_random_things[1:2]) #prints 3.4

#we can also use in and not in in boolean

print('this' in 'this is a string') #returns true
print('isa' in 'this is a string')#returns false

#diffrerence between list and string is :list can be modified but string cannot be modified
#Mutability is defined as whether an object can be modified its value after it has been created or not
# list is mutable whereas string isnt mutable
#order is defined as whether the order of the elements matter while accesing it
#both list and string are ordered


#mutable
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst) #prints ['one', 2, 3, 4, 5]

#immutable
#greeting = "Hello there"
#greeting[0] = 'M'
#print(greeting) # TypeError: 'str' object does not support item assignment

#methods in lists
#join
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["Rejina", "Dahal"])
print(name) #prints  Rejina-Dahal

#append
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters) #prints ['a', 'b', 'c', 'd', 'z']




