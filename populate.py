def directions():
    """
    This function creates a list of available directions.
    """
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu_and_input():
    """
    This function displays a menu of available directions, prompts the user to select one,
    and returns the corresponding direction.
    """
    print("Please select a direction:")
    available_directions = directions()

    for index, direction in enumerate(available_directions):
        print(f"{index}: {direction}")

    user_choice = int(input("Enter your choice (index): "))
    return available_directions[user_choice]


def run_task4():
    """
    This function simulates navigating an escape route by repeatedly prompting the user to select a direction
    and adding the selected direction to a list representing the escape route.
    """
    escape_route = []

    print("Working out escape route...")
    for _ in range(5):
        next_direction = menu_and_input()
        escape_route.append(next_direction)

    print(f"Escape route: {escape_route}")


run_task4()
