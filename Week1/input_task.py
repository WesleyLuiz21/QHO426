print("Please enter your name")
name = input()
print(f"Hello {name}")

print("Please enter your age")
age = int(input()) # Integer only, not float number.
print(f"Your age is {age}") # adds age to the console

print("please enter your Weight")
weight = float(input())
print(f"Your weight is {weight}")

print("please enter your Height")
height = float(input())
print(f"Your Height is {height}")

bmi = weight / (height * 2)
print(f"{name} your BMI is {bmi}")
