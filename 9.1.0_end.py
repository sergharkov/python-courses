class Person:
    def __init__(self,first_name, last_name):
        self.first_name=first_name.title()
        self.last_name=last_name.title()
    @property    
    def full_name(self):
        return self.first_name + " " + self.last_name
    @property
    def initials(self):
        return self.first_name[0].upper() + " " + self.last_name[0].upper()
    
    @full_name.setter
    def full_name(self, name):
        first,last = name.split(' ')
        self.first_name=first.title()
        self.last_name=last.title()
    
    @full_name.deleter
    def full_name(self):
        self.first_name=None
        self.last_name=None
                                


c=Person('sergii','kharkov')
print(c.full_name)
print(c.initials)

c.first_name="Igor"


print(c.full_name)
print(c.initials)

c.full_name="Roman Petrovich"
print(c.full_name)
print(c.initials)

del c.full_name
print(c.first_name , c.last_name)

print("-----------------------------------")
spisok = [16, 46, 26, 36]
for i in enumerate(spisok):
    print(i)



