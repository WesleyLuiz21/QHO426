# User Functions

def listen():
    response = input('Please enter a word representing a sound:')
    print(f'That was a loud {response}!')

listen()


# Exercise 2

def identify():
    response2 = input('What do you see?')
    print(response2)

    if response2 == 'a large boulder':
        print(f'Its time to run!')
    else:
        print('We will be fine')

identify()