
def backtrack(solution, choices, is_valid, is_complete):
    if is_complete(solution):
        print("Solution:", solution)
        return True

    for choice in choices:
        solution.append(choice)

        if is_valid(solution):
            if backtrack(solution, choices, is_valid, is_complete):
                return True

        solution.pop()

    return False


# Example: Find a sequence of 3 distinct numbers
# from the range 1 to 3.

def is_valid(solution):
    return len(solution) == len(set(solution))


def is_complete(solution):
    return len(solution) == 3


solution = []

if not backtrack(solution, [1, 2, 3], is_valid, is_complete):
    print("No solution found")
