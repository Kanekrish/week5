def movements():
    """
    This function creates a list of movement instructions.
    """
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    """
    This function simulates movement based on the instructions provided by the movements() function.
    """
    print("Moving...")

    movement_instructions = movements()

    for i in range(0, len(movement_instructions), 2):
        direction = movement_instructions[i]
        steps = movement_instructions[i + 1]
        print(f"{direction} for {steps} steps")

    # Call the run_task2 function to execute the movement simulation
    run_task2()
