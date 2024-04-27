#it refers to methods/functions/operators with the 
# same name that can be executed on many objects or classes.

#Function Polymorphism
#len() function.
#string

x = "Hello World!"

print(len(x)) #prints 12


#tuple
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))  #prints 3

#dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict)) #prints  3


#class polymorphism
class Animal: #parent class
    def make_sound(self):
        pass

class Dog(Animal): #child class
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"


def make_animal_sound(animal):
    return animal.make_sound()


dog = Dog()
cat = Cat()
bird = Bird()


print(make_animal_sound(dog))   # Output: Woof!
print(make_animal_sound(cat))   # Output: Meow!
print(make_animal_sound(bird))  # Output: Chirp!



