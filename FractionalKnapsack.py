def get_optimal_value(capacity, weights, values, names):
    size = len(weights)
    vpw = [(values[i] / weights[i], weights[i], names[i]) for i in range(size)]
    densities = sorted(vpw, reverse = True)

    finalValue = 0
    for i, v in enumerate(densities):
        a = min(capacity, densities[i][1])
        finalValue += a * densities[i][0]
        print(densities[i][2], a, "gram is taken")
        capacity -= a
    return finalValue

capacity = 220
values = [50000, 100000, 600000, 750000, 300000, 200000, 350000, 80000, 550000, 90000]
weights = [50, 10, 30, 25, 15, 40, 35, 20, 55, 45]
names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
opt_value = get_optimal_value(capacity, weights, values, names)
print("Value of the knapsack is", opt_value)

