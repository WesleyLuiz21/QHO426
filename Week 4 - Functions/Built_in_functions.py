print("Program Started!")

user_response = input("Please enter a standard character: ")

if len(user_response) == 1:
    i = ord(user_response)
    print(f"The ASCII code for the {user_response} is {i} is the letter entered by the user and {i} is the ASCII code as number")
else:
    print("Program Error 404!")

print("Program Ended!")