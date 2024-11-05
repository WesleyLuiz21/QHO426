user_response = int(input("How many rows should it have? "))
user_response2 = int(input("How many columns should it have?\n"))

for i in range(user_response):
    for j in range(user_response2):
        print(":-)", end=" ")
    print()