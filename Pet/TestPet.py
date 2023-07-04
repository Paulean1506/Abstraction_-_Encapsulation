# Write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet.
# This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

from Pet_Class import Pet
from termcolor import colored

class TestPet:
 def display_visual(pet):
    animal_type = pet.get_animal_type()
    name = pet.get_name()
    age = pet.get_age()

    print(colored("  \_/", "magenta"))
    print(colored(" (^_^)", "magenta"))
    print(colored(f" / {animal_type}", "magenta"))
    print(colored(f"{name}", "cyan"))
    print(colored(f"Age: {age} years", "yellow"))

def main():
    pet = Pet()

    print(colored("Enter the details of your pet:", "cyan"))
    pet.set_name(input("Name: "))
    pet.set_animal_type(input("Animal Type: "))
    pet.set_age(input("Age: "))

    print(colored("\nPet Details:", "cyan"))
     display_visual(pet)

if __name__ == "__main__":
    main()
