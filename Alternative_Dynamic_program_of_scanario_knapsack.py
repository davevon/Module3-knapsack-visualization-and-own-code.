import matplotlib.pyplot as plt

def knapsack_visualization(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dynamic programming table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

            # Plot the current state of the dynamic programming table
            plot_knapsack_state(dp, weights, values, i, w)

    return dp[n][capacity]

def plot_knapsack_state(dp, weights, values, i, w):
    plt.clf()
    plt.title("Knapsack Dynamic Programming")
    plt.xlabel("Capacity")
    plt.ylabel("Value")

    # Plot items
    plt.scatter(weights[:i], values[:i], color='blue', label="Items")

    # Plot the knapsack state
    for j in range(i):
        plt.annotate(f"({weights[j]}, {values[j]})", (weights[j], values[j]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f"Current Weight: {w}", (weights[i-1], values[i-1]), textcoords="offset points", xytext=(0,-30), ha='center')
    plt.annotate(f"Current Value: {dp[i][w]}", (weights[i-1], values[i-1]), textcoords="offset points", xytext=(0,-50), ha='center')
    plt.annotate(f"Previous Value: {dp[i-1][w]}", (weights[i-1], values[i-1]), textcoords="offset points", xytext=(0,-70), ha='center')

    # Plot the knapsack capacity
    plt.axvline(x=w, color='red', linestyle='--', label="Knapsack Capacity")

    # Plot the dynamic programming table
    for j in range(i + 1):
        for k in range(w + 1):
            if dp[j][k] > 0:
                plt.annotate(dp[j][k], (k, dp[j][k]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.legend(loc="lower right")
    plt.show()
    plt.pause(0.1)

# Example usage
weights = [ 2, 1, 4, 1, 12]  
values = [ 2, 1, 10, 2, 4]
capacity = 15

max_value = knapsack_visualization(weights, values, capacity)
print("Maximum value:", max_value)
