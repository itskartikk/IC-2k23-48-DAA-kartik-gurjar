
def fractional_knapsack(profit, weight, capacity):
    n = len(profit)

    # Calculate profit/weight ratio
    items = []

    for i in range(n):
        ratio = profit[i] / weight[i]
        items.append((ratio, profit[i], weight[i]))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_profit = 0

    print("Selected Items:")

    for ratio, p, w in items:

        if capacity == 0:
            break

        if w <= capacity:
            # Take the complete item
            total_profit += p
            capacity -= w

            print("Full item selected:", p, w)

        else:
            # Take fractional part
            fraction = capacity / w

            total_profit += p * fraction

            print("Fraction selected:", round(fraction, 2))

            capacity = 0

    return total_profit


# Main program
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

result = fractional_knapsack(profit, weight, capacity)

print("\nMaximum Profit:", result)
