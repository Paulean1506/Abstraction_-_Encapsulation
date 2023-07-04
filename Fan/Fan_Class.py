# Paulean Marguerette F. Parrish
# BSCPE 1-4
# (The Fan class).  Design a class named Fan to represent a fan. The class contains:

# Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed=1, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # The accessor(getters)  and mutator(setters)  methods for all four data fields.
    # A private int data field named speed that specifies the speed of the fan.
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    # A private bool data field named on that specifies whether the fan is on (the default is False).
    def is_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on

    # A private float data field named radius that specifies the radius of the fan.
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    # A private string data field named color that specifies the color of the fan.
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
