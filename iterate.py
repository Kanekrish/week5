def directions():
    """
    This function creates a list of available directions.
    """
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu():
    """
    This function displays a menu of available directions and allows the user to select one.
    """
    print("Please select a direction:")
    available_directions = directions()

    for index, direction in enumerate(available_directions):
        print(f"{index}: {direction}")


def run_task3():
    """
    This function runs the interactive menu for selecting directions.
    """
    menu()


if __name__ == "__main__":
    run_task3()
