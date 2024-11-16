def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right", ]
    return steps

def menu():
    print("Please select a direction:")
    step = directions()

    for i in range(len(step)):
        print(f"{i}: {step[i]}")

def run_task3():
    menu()

if __name__ == "__main__":
    run_task3()