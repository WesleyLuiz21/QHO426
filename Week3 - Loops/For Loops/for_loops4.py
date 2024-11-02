print("Please enter a word")
user_word = input()

print("\nDisplaying index positions...")

for position in range(len(user_word)):
    print(f"index {position}: {user_word[position]}")

print("\nDone!")
