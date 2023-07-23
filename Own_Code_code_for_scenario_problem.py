import matplotlib.pyplot as plt

def knapsack(cars, weight_limit):
    n = len(cars)
    dp = [[0] * (weight_limit + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, weight_limit + 1):
            if cars[i - 1]['weight'] <= j:
                dp[i][j] = max(cars[i - 1]['value'] + dp[i - 1][j - cars[i - 1]['weight']], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_cars = []
    i = n
    j = weight_limit
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_cars.append(cars[i - 1])
            j -= cars[i - 1]['weight']
        i -= 1

    return selected_cars

def visualize_knapsack(cars, selected_cars, weight_limit):
    names = [car['name'] for car in cars]
    weights = [car['weight'] for car in cars]
    values = [car['value'] for car in cars]

    plt.figure(figsize=(8, 6))
    plt.title('Knapsack Algorithm - Car Selection')
    plt.xlabel('Weight')
    plt.ylabel('Value')
    plt.scatter(weights, values, label='Cars')
    plt.scatter([car['weight'] for car in selected_cars], [car['value'] for car in selected_cars], color='red', label='Selected Cars')

    for i, name in enumerate(names):
        plt.annotate(name, (weights[i], values[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
cars = [
      {'name': 'Car 1', 'weight': 2, 'value': 2},
    {'name': 'Car 2', 'weight': 1, 'value': 1},
    {'name': 'Car 3', 'weight': 4, 'value': 10},
    {'name': 'Car 4', 'weight': 1, 'value': 2},
    {'name': 'Car 5', 'weight': 12, 'value':4}
]

weight_limit = 15

selected_cars = knapsack(cars, weight_limit)

print("Selected Cars:")
for car in selected_cars:
    print(f"- {car['name']} (Weight: {car['weight']}, Value: {car['value']})")
    


visualize_knapsack(cars, selected_cars, weight_limit)
max_value = knapsack_visualization(Value)
print("Maximum value:", max_value)
