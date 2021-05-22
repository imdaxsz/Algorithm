S = 'cereal'
T = 'caramel'

def edit_distance(S, T):
    s = list(S)
    t = list(T)
    m = len(s)
    n = len(t)
    E = []

    for i in range(m+1):
        E.append([0 for j in range(n+1)])
        E[i][0] = i
    for j in range(n+1):
        E[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            a = 0 if s[i-1] == t[j-1] else 1
            E[i][j] = min((E[i][j-1]+1),(E[i-1][j]+1),(E[i-1][j-1]+a))

    return E[m][n]


E = edit_distance(S, T)
print("S: ", S)
print("T: ", T)
print(E)

