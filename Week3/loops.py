i = 0 # variable to count the number of iterations

while i < 10: # to display the count
    i = i + 1
    print(f"{i}") # printing each number to the console

print(f"completed {i}!")

# Exercise 1:

number = int(input("How many apples should I remove?")) # ask the user for the number of apples

j = 0 # declares the number of iterations
while j < number: # keep the loop running while the iteration number is less than the user input
    j = j + 1
    print(f"removed apple.")

print(f"completed {j}!")