def likelihood():
    """
    This function calculates the step with the minimum likelihood of falling.
    """
    step_likelihoods = (50, 38, 27, 99, 10)
    min_likelihood_index = step_likelihoods.index(min(step_likelihoods))
    min_likelihood_step = min_likelihood_index + 1
    return min_likelihood_step


def run_task1():
    """
    This function determines and displays the step with the minimum likelihood of falling.
    """
    step_with_minimum_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {step_with_minimum_likelihood}%")


# Call the run_task1 function to execute the task
if __name__ == "__main__":
    run_task1()
