
def display_chars(path,num):
    file = open("library.txt")
    
    with open ("library.txt") as file:
        data = file.read()
        lines = data.split('\n')
print