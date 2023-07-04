# Write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet.
# This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

from Pet_Class import Pet
from termcolor import colored

from termcolor import colored

class TestPet:
    @staticmethod
    def display_visual(pet):
        animal_type = pet.get_animal_type()
        name = pet.get_name()
        age = pet.get_age()

        print(colored("  \_/", "magenta"))
        print(colored(" (^_^)", "magenta"))
        print(colored(f" / {animal_type}", "magenta"))
        print(colored(f"Name: {name}", "red"))
        print(colored(f"Age: {age} years", "yellow"))

    @staticmethod
    def main():
        pet = Pet()

        print(colored("\033[1;33m\nEnter the details of your pet:", "cyan"))
        pet.set_name(input("\033[1;34mName: "))
        pet.set_animal_type(input("\033[1;35mAnimal Type: "))
        pet.set_age(input("\033[1;36mAge: "))

        print(colored("\033[1;37m\nPet Details:", "cyan"))
        TestPet.display_visual(pet)


if __name__ == "__main__":
    TestPet.main()
