class Robot:

    # Class Attribute
    MAX_ENERGY = 100
     
    # Initializer Method
    def __init__(self):
        self.name = "Robot"
        self.energy = 20
    #Instance Method
    def display(self):
        print(f"I am {self.name} and my energy level is {self.energy} out of {Robot.MAX_ENERGY}")

if __name__ == "__main__":
    robot1 = Robot()
    robot1.display()