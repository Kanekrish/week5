def likelihood_min_max():
    """
    This function calculates the minimum and maximum likelihoods of falling from a tuple of likelihoods.
    """
    step_likelihoods = (50, 38, 27, 99, 4)
    min_likelihood = min(step_likelihoods)
    max_likelihood = max(step_likelihoods)
    return min_likelihood, max_likelihood


def run_task2():
    """
    This function determines and displays the minimum and maximum likelihoods of falling.
    """
    min_likelihood, max_likelihood = likelihood_min_max()
    print(f"Minimum likelihood of falling: {min_likelihood}%")
    print(f"Maximum likelihood of falling: {max_likelihood}%")


# Call the run_task2 function to execute the task
if __name__ == "__main__":
    run_task2()
    