#for loops 
# is iterable that is it can return its elements one at a time

cities = ['dharan', 'damak', 'biratnagar', 'janakpur']
for city in cities:
    print(city)   # prints dharan damak  biratnagar janakpur  
 
 #range
 
for i in range(3):
    
    print("Hello")   #prints Hello Hello Hello
    
#range(start=0, stop, step=1)

for num in range(1, 10, 2):
    print(num, end=' ')  # prints  1 3 5 7 9

#replace
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(name) #prints phoebe_buffay



#while loops :indefinite iteration which is when a loop
# repeats an unknown number of times and ends when some condition is met

#factorial using while loops
number = 6
product = 1
current = 1

while  current <= number:
    product *= current
    current += 1


print(product) #prints 720