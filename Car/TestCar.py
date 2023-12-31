# Design a program that creates a Car object
from Car_Class import Car
import time
from termcolor import colored

class TestCar:
    def display_speed(self):
        speed = self.get_speed()
        color = "green" if speed > 0 else "red"
        visual = f"Current Speed: {speed} mph"
        print(colored(visual, color))

def display_visual(car):
    speed = car.get_speed()
    if speed > 0:
        print(colored("    ______", "yellow"))
        print(colored(" __/|___|__\\___", "yellow"))
        print(colored("|______________|", "yellow"))
        print(colored(f"|     {speed} mph   |", "yellow"))
        print(colored("|______________|", "yellow"))
        print(colored("   (o)    (o)", "yellow"))
    else:
        print(colored("    ______", "yellow"))
        print(colored(" __/|___|__\\___", "yellow"))
        print(colored("|______________|", "yellow"))
        print(colored("| STOPPED 0 mph|", "yellow"))
        print(colored("|______________|", "yellow"))
        print(colored("   (x)    (x)", "yellow"))


# Call the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it. 
def main():
    car = Car("2023", "Ford Mustang")

    print(colored("\nAccelerating...", "green"))
    for _ in range(5):
        car.accelerate()
        display_visual(car)
        time.sleep(1)

# Call the brake method five times. 
# After each call to the brake method, get the current speed of the car and display it.
    print(colored("\nBraking...", "red"))
    for _ in range(5):
        car.brake()
        display_visual(car)
        time.sleep(1)

if __name__ == "__main__":
    main()