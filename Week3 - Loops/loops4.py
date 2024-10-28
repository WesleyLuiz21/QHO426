# get user response
user_response = input("Please enter a phrase:")

i = 0 # counter

while i < len(user_response): # while the counter is less than the number inputted by the user
    print("Hi ", end="")
    i += 1

print(f"\nNumber of characters: {i}")