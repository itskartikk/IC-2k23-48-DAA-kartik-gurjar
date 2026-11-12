
import heapq


def knapsack_branch_bound(weights, profits, capacity):
    n = len(weights)

    # Sort items by profit-to-weight ratio
    items = sorted(
        zip(weights, profits),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    weights = [item[0] for item in items]
    profits = [item[1] for item in items]

    def bound(level, weight, profit):
        if weight >= capacity:
            return profit

        result = profit
        total_weight = weight
        j = level + 1

        # Add complete items
        while j < n and total_weight + weights[j] <= capacity:
            total_weight += weights[j]
            result += profits[j]
            j += 1

        # Add fractional part for upper bound
        if j < n:
            result += (capacity - total_weight) * (
                profits[j] / weights[j]
            )

        return result

    # Priority queue: highest bound first
    pq = []

    best_profit = 0
    best_items = []

    initial_bound = bound(-1, 0, 0)

    heapq.heappush(
        pq, (-initial_bound, 0, 0, -1, [])
    )

    while pq:
        neg_bound, profit, weight, level, selected = heapq.heappop(pq)

        current_bound = -neg_bound

        if current_bound <= best_profit:
            continue

        if level == n - 1:
            continue

        next_level = level + 1

        # Branch 1: Include next item
        new_weight = weight + weights[next_level]
        new_profit = profit + profits[next_level]

        if new_weight <= capacity:
            if new_profit > best_profit:
                best_profit = new_profit
                best_items = selected + [next_level]

            new_bound = bound(
                next_level, new_weight, new_profit
            )

            if new_bound > best_profit:
                heapq.heappush(
                    pq,
                    (-new_bound, new_profit, new_weight,
                     next_level, selected + [next_level])
                )

        # Branch 2: Exclude next item
        exclude_bound = bound(
            next_level, weight, profit
        )

        if exclude_bound > best_profit:
            heapq.heappush(
                pq,
                (-exclude_bound, profit, weight,
                 next_level, selected.copy())
            )

    original_items = [
        items[i] for i in best_items
    ]

    print("Maximum Profit:", best_profit)
    print("Selected Items (Weight, Profit):", original_items)


n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))

capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or len(weights) != n or len(profits) != n:
    print("Invalid input")
elif any(w <= 0 for w in weights) or any(p < 0 for p in profits):
    print("Weights must be positive and profits non-negative")
else:
    knapsack_branch_bound(weights, profits, capacity)
