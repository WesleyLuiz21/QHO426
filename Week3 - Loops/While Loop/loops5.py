
print("Calculating the sum of the first 100 numbers...")

i = 0 # declares the counter variable
sum_numbers = 0 # declares the numbers to be summed and looped

while i < 100: # sets the program to stop when it reaches 100 iterations
    i = i + 1 # tracks the iteration number in order to get to 100 iterations
    sum_numbers = sum_numbers + i # sum up the numbers at each iteration

print(f"...Done! the answer is {sum_numbers}")