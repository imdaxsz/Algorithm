import sys

d = [10, 20, 5, 15, 30]
n = 4

def order(i, j, O):
    if (i==j):
        print("A%d"%i, end="")
    else:
        k = O[i][j]
        print("(", end="")
        order(i, k, O)
        order(k+1, j, O)
        print(")", end="")

def matrixChain(d, n):
    C = []
    O = []
    for i in range(n+1):
        C.append([0 for j in range(n+1)])
        O.append([0 for j in range(n+1)])

    for i in range(1, n+1):
        C[i][i] = 0

    for L in range(1, n): # L 은 부분 문제의 크기를 조절하는 인덱스이다
        for i in range(1, n - L + 1):
            j = i + L
            C[i][j] = sys.maxsize
            for k in range(i, j):
                temp = C[i][k] + C[k+1][j] + d[i-1]*d[k]*d[j]
                if temp < C[i][j]:
                    C[i][j] = temp
                    O[i][j] = k

    return C[1][n], O

count, O = matrixChain(d, n)
print("d:", d)
print("count:", count)
print("order: ", end="")
order(1, n, O)
