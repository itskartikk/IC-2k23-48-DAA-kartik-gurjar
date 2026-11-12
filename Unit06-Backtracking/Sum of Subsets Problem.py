
def sum_of_subsets(arr, target):
    arr.sort()
    result = []

    def backtrack(index, current, current_sum):
        if current_sum == target:
            result.append(current.copy())
            return

        if current_sum > target or index == len(arr):
            return

        # Include the current element
        current.append(arr[index])

        backtrack(
            index + 1,
            current,
            current_sum + arr[index]
        )

        # Exclude the current element
        current.pop()

        # Skip duplicate values
        next_index = index + 1
        while next_index < len(arr) and arr[next_index] == arr[index]:
            next_index += 1

        backtrack(next_index, current, current_sum)

    backtrack(0, [], 0)

    return result


arr = list(map(int, input("Enter set elements: ").split()))
target = int(input("Enter target sum: "))

if any(x <= 0 for x in arr):
    print("Please enter positive integers only.")
else:
    subsets = sum_of_subsets(arr, target)

    if subsets:
        print("Subsets with target sum", target, ":")
        for subset in subsets:
            print(subset)
    else:
        print("No subset found")
