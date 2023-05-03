from objeto import Car

car_1 = Car("Chevy",2021,"Blue")
Car.ruedas = 2
print(Car.ruedas)
print(car_1.modelo)
print(car_1.anio)
print(car_1.color)
car_1.conducir()