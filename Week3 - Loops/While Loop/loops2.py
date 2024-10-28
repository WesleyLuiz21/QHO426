user_response = int(input("How many obstacles must I avoid?"))

i = 0 # counter

while i < user_response:
    print("Avoiding...")
    i += 1
    print(f"...Done! {i} obstacles avoided!")

print("All obstacles have been avoided.")