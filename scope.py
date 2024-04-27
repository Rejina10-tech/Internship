#variable is only created whrere it is created
#local scope 
 
def myfunc():
  x = 300
  print(x) #prints 300

myfunc() 

#global
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)