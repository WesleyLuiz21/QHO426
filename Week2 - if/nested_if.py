book = str(input("Please enter the type cover type of the book:"))

if book == "soft":
    book_condition = str(input("Is the book perfect bound?"))
    if book_condition == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif book == "hard":
    print("Books with hard covers can be more expensive!")

