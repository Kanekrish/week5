def steps():
    """
    This function creates a list of tuples containing step names and their corresponding likelihoods.
    """
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4),
    ]
    return likelihoods


def run_task3():
    """
    This function analyzes the likelihood of falling for each step and categorizes them into good or bad steps.
    """
    step_likelihoods = steps()
    good_steps = []
    bad_steps = []

    for step_name, likelihood in step_likelihoods:
        if likelihood >= 50:
            bad_steps.append((step_name, likelihood))
        else:
            good_steps.append((step_name, likelihood))

    num_good_steps = len(good_steps)
    num_bad_steps = len(bad_steps)
    print(
        f"Good steps: {good_steps}, Bad steps: {bad_steps}"
        f"\nTotal good steps: {num_good_steps}, Total bad steps: {num_bad_steps}"
    )


# Call the run_task3 function to execute the task
if __name__ == "__main__":
    run_task3()
