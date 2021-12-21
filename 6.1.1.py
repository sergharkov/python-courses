class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def get_greeting(self):
        return F"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old"   
    def talk(self):
        print(self.get_greeting())
x=Person("Carl","Johnson","26")  
x.talk()
