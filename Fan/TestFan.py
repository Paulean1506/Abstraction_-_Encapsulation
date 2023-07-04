# Write a test program named TestFan that creates two Fan objects. 

# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
from Fan_Class import Fan

class TestFan:
    @staticmethod
    def main():
        fan1 = Fan(Fan.FAST, 10, "yellow", True)
        print("\033[1;33mFan 1:\033[0m")
        print("\033[1;34mSpeed:\033[0m", fan1.get_speed())
        print("\033[1;35mRadius:\033[0m", fan1.get_radius())
        print("\033[1;36mColor:\033[0m", fan1.get_color())
        print("\033[1;37mOn:\033[0m", fan1.is_on())
        print("\033[1;32mVisual:\033[0m")
        print(TestFan.render_fan(fan1))