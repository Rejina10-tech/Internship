class Student:  #parent class
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

class HighSchoolStudent(Student):#child class
    def __init__(self, name, age, grade, year):
        super().__init__(name, age, grade)
        self.year = year

    def display_info(self):  # Override display_info method
        super().display_info()
        print(f"Year: {self.year}")

