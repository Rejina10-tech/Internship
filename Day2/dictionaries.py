#dictionary is a mutable data type that stores mappings of 
# unique keys to values

elements = {"hydrogen": 1,
            "helium": 2, 
            "carbon": 6}

print(elements["helium"])  # print the value mapped to "helium" that is 2
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print(elements)# {'hydrogen': 1, 'helium': 2, 'carbon': 6, 'lithium': 3}


#in and get in dict
print("carbon" in elements) #prints true
print(elements.get("dilithium")) #prints none

#Identity operators
#is and not is

n = elements.get("dilithium")
print(n is None) #prints True
print(n is not None) #prints False
