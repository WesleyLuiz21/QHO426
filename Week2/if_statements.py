print("What type of book do you like?")

# Taking the user input and storing in a variable called book
book = input()

if book == "adventure":
    print("I like adventure books!")
else:
    print("Wrong input by user")

print("Finished reading book.")

# Second Task

print("Please enter the activity to be performed.")

activity = input()

if activity == "calculate":
    print("Performing calculations...")
else:
    print ("Wrong input by user")
print("Activity completed!")

# Third Task

print("Towards which direction should I go (up, down, right, left)?")

direction = input()

if direction == "up":
    print("moving in an upward direction!")
elif direction == "down":
    print("moving in an downward direction!")
elif direction == "right":
    print("moving in an right direction!")
elif direction == "left":
    print("moving in an left direction!")
else:
    print("Wrong input by user")