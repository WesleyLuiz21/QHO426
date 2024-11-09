print("Program Started")

response = input("Please enter an ASCII code: ")

# Convert input to an integer and take the absolute value
conversion = abs(int(response))

# Check if the conversion is within the printable ASCII range
if conversion in range(32, 127):
    answer = chr(conversion)
    print(f"The character represented by the ASCII code {conversion} is '{answer}'.")
else:
    print("Error 404: The number entered is outside the printable ASCII range (32-126).")

print("Program Ended")
