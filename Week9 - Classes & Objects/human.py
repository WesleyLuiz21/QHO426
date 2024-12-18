class Human:

    # Class Atribute

    MAX_ENERGY: 100

    #Initializer Method
    def __init(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name} and my age is {self.age}")

    # String Representation
    def __str__(self):
            return f"Human={self.name}, age{self.age}, energy={self.energy}"
    
    def __repr__(self):
         return f"Human(name={self.name}, age={self.age}, energy={self.energy})"
    
if (__name__ == "__main__"):
    human1 = Human()
    human1.display()