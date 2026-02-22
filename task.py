import random

def run_automation_task():
    """
    Simulates a real automation task.
    Sometimes succeeds, sometimes fails.
    """

    possible_errors = [
        "API_TIMEOUT",
        "AUTH_EXPIRED",
        "INVALID_SCHEMA",
        None  # success
    ]

    error = random.choice(possible_errors)

    if error:
        raise Exception(error)

    return "Automation task executed successfully"
