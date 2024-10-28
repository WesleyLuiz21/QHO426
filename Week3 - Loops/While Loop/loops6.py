# getting user response
user_response = int(input("How many numbers should I sum up?"))

i = 0 # counter
sum_numbers = 0

while i < user_response:
    i += 1 # increases the counter at each iteration according to the user response variable
    user_response2 = int(input(f"Please enter number {i} of {user_response}:")) # gets the second user input
    sum_numbers += user_response2 # sums the number inputted by the user and save in our variable

print(f"The answer is {sum_numbers}.")
