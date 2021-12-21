class Animal:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        raise NoImplementedError("Must implement")
    
    def animal_talk(inst):
        pass 

class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("meow")
        



cat= Cat('tom')
dog= Dog('muhtar')
cat.talk()
dog.talk()
       

