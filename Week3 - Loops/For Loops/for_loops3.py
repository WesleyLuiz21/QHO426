user_response = int(input("What level of brightness is required? "))

if user_response % 2 != 0:
    print("Please enter a valid level of brightness")
    user_response = int(input("What level of brightness is required? "))

print("\nAdjusting brightness...\n")

for i in range(2, user_response, 2):
    print(f"Brightness: {"*" * i}")

print("\nComplete!")