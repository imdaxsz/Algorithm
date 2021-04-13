def euclid(a, b):
    if (b == 0):
        return a
    else:
        return euclid(b, a%b)

a, b = eval(input("두 정수 입력 : "))

print("최대공약수 :", euclid(a,b))


