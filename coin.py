change = int(input("거스름돈을 입력하세요: "))

n500 = 0
n170 = 0
n100 = 0
n50 = 0
n10 = 0


def Coin500(change, n500):
    if change >= 500:
        n500 = change // 500
        change = change % 500
    return change, n500

def Coin170(change, n170):
    if change >= 170:
        n170 = change // 170
        change = change % 170
    return change, n170


def Coin100(change, n100):
    if change >= 100:
        n100 = change // 100
        change = change % 100
    return change, n100

def Coin50(change, n50):
    if change >= 50:
        n50 = change // 50
        change = change % 50
    return change, n50

def Coin10(change, n10):
    if change >= 10:
        n10 = change // 10
        change = change % 10
    return change, n10


change, n500 = Coin500(change, n500)
change, n170 = Coin170(change, n170)
change, n100 = Coin100(change, n100)
change, n50 = Coin50(change, n50)
change, n10 = Coin10(change, n10)


print(n500, n170, n100, n50, n10)
print(n500 + n170 + n100 + n50 + n10)