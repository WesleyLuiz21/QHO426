user_response = str(input("Where should I look? "))
if user_response == "in the bedroom":
    user_response2 = str(input("Where in the bedroom should I look?"))

    if user_response2 == "under the bed":
        print("Found some shoes but no phone")
elif user_response == "in the bathroom":
    user_response3 = str(input("Where in the bathroom should I look?"))
    if user_response3 == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")
elif user_response == "in the living room":
    user_response4 = str(input("Where in the living room should I look?"))
    if user_response4 == "on the table":
        print("Yes! found my phone!")
    else:
        print("Found some stuff but no phone")
else:
    print("I do not know where that is but I will keep looking")

