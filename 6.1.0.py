class Car():
    total_number_cars = 0
    def __init__(self, brand,model,year,color):
        self.brand = brand
        self.mode = model
        self.year = year
        self.color = color
        self.total_driver_km = 0
        Car.total_number_cars += 1
    def repain(self, color):
        self.color=color
    def drive(self, km_driven):
        self.total_driver_km +=km_driven
volvocar1= Car('Volvo','cx90','2017','black')
volvocar2= Car('Volvo1','cx901','20171','black1')
print(volvocar1.brand, volvocar1.color)

volvocar1.repain('blue')

print(volvocar2.brand, volvocar2.color)
