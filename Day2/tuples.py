
#tuples are  data types for imuutable oredered sequences of elements
#they are useful when two/more values are close to each other like lattitude and longitude

damak = (26, 87)

print(type(damak))  #prints  <class 'tuple'>
print("Damak is at latitude: {}".format(damak[0])) #Damak is at latitude: 26
print("Damak is at longitude: {}".format(damak[1]))#Damak is at longitude: 87

#Tuples can be used to assign multiple variables in a compact way
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height)) #The dimensions are 52 x 40 x 100


