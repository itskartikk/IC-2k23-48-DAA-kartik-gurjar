
def job_sequencing(jobs):
    # Sort jobs according to profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Initialize time slots
    slots = [None] * max_deadline

    total_profit = 0

    # Schedule jobs
    for job_id, deadline, profit in jobs:

        # Find an available slot before deadline
        for j in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    print("Scheduled Jobs:")

    for i in range(max_deadline):
        if slots[i] is not None:
            print("Time Slot", i + 1, ":", slots[i])

    print("\nMaximum Profit:", total_profit)


# Main program
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_sequencing(jobs)
