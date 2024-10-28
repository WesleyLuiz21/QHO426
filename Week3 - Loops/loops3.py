# Gets input from user
user_input = int(input("How many bars should be charged?"))

bar_number = 0 # counter

while bar_number < user_input:
    bar_number += 1
    print("Charging: ", end="")
    print(f"{"█ " * bar_number}") # displays the symbol rather than the number itself

print("\nThe battery is fully charged.")