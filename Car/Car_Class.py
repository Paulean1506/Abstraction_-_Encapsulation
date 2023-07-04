# Paulean Marguerette F. Parrish
# BSCPE 1-4
# Write a class named Car that has the following data attributes:
# _ _year_model (for the car’s year model)
# _ _make (for the make of the car)
# _ _speed (for the car’s current speed)
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    #The class should also have the following methods:
    # accelerate() The accelerate method should add 5 to the speed data attribute each time it is called.
    def accelerate(self):
        self.__speed += 5
    
    # brake() The brake method should subtract 5 from the speed data attribute each time it is called.
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
    
    # get_speed() The get_speed method should return the current speed.
    def get_speed(self):
        return self.__speed

    


