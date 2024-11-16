def display_ladder(steps):
    for steps in range(1, steps + 1):
        print("| |")
        print("***")

def create_ladder():
    response = int(input("How many steps remaining?\n"))
    display_ladder(response)

print("Function finished!")

create_ladder()