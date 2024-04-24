#set is a data type for mutable unordered collections of unique elements.
#One application of a set is to quickly remove duplicates from a list.

countries = ['India', 'United States', 'India', 'China', 'Sweden', 
             'Nepal']
print(len(countries))  #prints 6
print(countries[:5])  #prints ['India', 'United States', 'India', 'China', 'Sweden']

country_set = set(countries)
print(country_set) 


country_set.add('Italy')
print(country_set) #{'China', 'United States', 'India', 'Nepal', 'Italy', 'Sweden'}

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element and prints false

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)


