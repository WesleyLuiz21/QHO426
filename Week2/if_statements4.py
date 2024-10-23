# Sixth task


first_number = int(input("Please enter the first whole number:"))
second_number = int(input("Please enter the second whole number:"))
third_number = int(input("Please enter the third whole number:"))

# counters for even and odd numbers

even_count = 0
odd_count = 0

# If statements for each variable. This can potentially be looped in the future.

if first_number % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if second_number % 2 ==0:
    even_count += 1
else:
    odd_count += 1

if third_number % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print(f"There were {even_count} even and {odd_count} numbers.")
