
def exhaustive_search(arr, capacity):
    n = len(arr)

    max_sum = 0
    best_subset = []

    # Generate all possible subsets
    for i in range(1 << n):
        subset = []
        total = 0

        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
                total += arr[j]

        # Check whether subset is valid
        if total <= capacity and total > max_sum:
            max_sum = total
            best_subset = subset

    return max_sum, best_subset


arr = list(map(int, input("Enter array elements: ").split()))
capacity = int(input("Enter maximum capacity: "))

max_sum, subset = exhaustive_search(arr, capacity)

print("Best Subset:", subset)
print("Maximum Sum:", max_sum)
