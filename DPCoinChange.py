import sys

def DPCoinChange(n, d):
    C = []
    coin_list = []
    k = len(d)

    for i in range(n+1):
        C.append(0)
        coin_list.append(0)
    for i in range(1, n+1):
        C[i] = sys.maxsize
    C[0] = 0

    for j in range(1, n+1):
        for i in range(1, k):
            if(d[i]<=j) and (C[j-d[i]]+1 < C[j]):
                C[j] = C[j-d[i]]+1
                coin_list[j] = d[i]

    return C[n], coin_list

def CountCoin(coin_list, n, d):
    coin = []
    change = n
    for i in range(len(d)):
        coin.append(0)

    while change > 0:
        for i in range(len(d)):
            if coin_list[change] == d[i]:
                coin[i] += 1
        change -= coin_list[change]

    for i in range(1, len(d)):
        print("%d원: %d개" % (d[i], coin[i]))

n = 25
d = [0, 16, 10, 5, 1]
result, coin_list = DPCoinChange(n, d)

print("n:", n)
print("d:", d)
print("result:", result)
CountCoin(coin_list, n, d)

