import os


def cwd():

    # Retrieve the current working directory
    path = os.getcwd()

    # Display the current working directory
    print(f"The current working directory is {path}")

    # List the contents of the current directory
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():

    print("Processing...")
    cwd()

# call the function run
run()
