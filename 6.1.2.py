class Dog:
    age_factor = 7
    def __init__(self, age):
        self.age = age
    def validate(self):
        try:
            if (type(self.age) is not float) and (type(self.age) is not int):
                raise TypeError           
            return self.age
        except  TypeError:
            f" TypeError "
            raise       
    def human_age(self):
        adge.validate()     
        humane_age_value = self.age * self.age_factor
        return round(humane_age_value,2)
adge=Dog("10")
print(adge.human_age())

