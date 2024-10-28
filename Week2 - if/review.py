user_response = str(input("Please enter the type of adventure:"))
user_response3 = str(input("Do I like adventures?"))
user_response4 = input("Do I like action movies?")

if user_response == "scary":
    user_response2 = str(input("should I keep going?"))
    if user_response2 == "yes":
        print("Oh no I see a monster")
    else:
        print("I should return.")
elif (user_response == "adventure") or (user_response == "action"):
    print("Lets goo!")
elif user_response4 == "yes":
    user_response4 = True
elif user_response4 == "no":
    user_response4 = False
elif (user_response == "drama") and (user_response3 == "no"):
    print("You are so dramatic oh my god")
elif (user_response == "drama") and (user_response3 == "yes"):
        print("maybe you should watch the titanic movie")
else:
    print("This genre is not allowed, get out of here!")
if not user_response4:
    print("Thank you!")