# Write a test program named TestFan that creates two Fan objects. 

from Fan_Class import Fan

class TestFan:
    @staticmethod
    def main():
        
        # For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
        fan1 = Fan(Fan.FAST, 10, "yellow", True)
        print("\033[1;33m\nFan 1:\033[0m")
        print("\033[1;34mSpeed:\033[0m", fan1.get_speed())
        print("\033[1;35mRadius:\033[0m", fan1.get_radius())
        print("\033[1;36mColor:\033[0m", fan1.get_color())
        print("\033[1;37mOn:\033[0m", fan1.is_on())
        print("\033[1;32mVisual:\033[0m")
        print(TestFan.render_fan(fan1))

        # Assign medium speed, radius 5, color blue, and turn it off for the second object.
        fan2 = Fan(Fan.MEDIUM, 5, "blue", False)
        print("\n\033[1;33mFan 2:\033[0m")
        print("\033[1;34mSpeed:\033[0m", fan2.get_speed())
        print("\033[1;35mRadius:\033[0m", fan2.get_radius())
        print("\033[1;36mColor:\033[0m", fan2.get_color())
        print("\033[1;37mOn:\033[0m", fan2.is_on())
        print("\033[1;32mVisual:\033[0m")
        print(TestFan.render_fan(fan2))

    # Display results with visuals
    @staticmethod
    def render_fan(fan):
        if fan.is_on():
            visual = r'''
                  __
             \\   _   //
          /   \\     //   \
         / /   \\   //   \ \
                \\ //
        =========| |=========
                // \\
         \ \   //   \\   / /
          \   //  _  \\   /
             //  __   \\
            '''
        else:
            visual = r'''
                 ||  
                 ||
                 ||
                 ||
        =========||==========
                 ||
                 ||
                 ||
                 ||
            '''

        return visual

if __name__ == "__main__":
    TestFan.main()

