def knapsack(capacity, n, weights, values):
    K = []
    for i in range(n+1):
        K.append([0 for j in range(capacity+1)])
        K[i][0] = 0
    for w in range(capacity+1):
        K[0][w] = 0

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w], K[i-1][w-weights[i-1]]+values[i-1])

    return K[n][capacity]

capacity = 10
values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
k = knapsack(capacity, 4, weights, values)
print(k)

