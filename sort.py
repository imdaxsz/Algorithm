import random

# 버블 정렬
def BubbleSort(L):
    for i in range(1, len(L)):
        for j in range(1, len(L)-i+1):
            if L[j-1] > L[j]:
                L[j-1], L[j] = L[j], L[j-1]
    return L


# 선택 정렬
def SelectionSort(L):
    for i in range(len(L)-1):
        min = i
        for j in range(i+1, len(L)):
            if(L[j] < L[min]):
                min = j
        L[i], L[min] = L[min], L[i]
    return L


# 삽입 정렬
def InsertionSort(L):
    for i in range(1, len(L)):
        currentElement = L[i]
        j = i-1
        while j >= 0 and L[j] > currentElement:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = currentElement
    return L


# 쉘 정렬
def ShellSort(L):
    gap = len(L)//2
    while(gap>0):
        for i in range(gap, len(L)):
            currentelement = L[i]
            j = i
            while (j>=gap) and (L[j-gap]>currentelement):
                L[j] = L[j-gap]
                j -= gap
            L[j] = currentelement
        gap //= 2
    return L


# 힙 정렬
def HeapSort(L):
    for i in range(1, len(L)):  # max heap
        k = i
        while k != 0:
            r = (k - 1) // 2
            if L[r] < L[k]:
                L[r], L[k] = L[k], L[r]
            k = r

    for j in range(len(L) - 1, -1, -1):
        L[0], L[j] = L[j], L[0]
        r = 0
        k = 1

        while k < j:
            k = 2 * r + 1
            if k < j - 1 and L[k] < L[k + 1]:
                k += 1

            if k < j and L[r] < L[k]:
                L[r], L[k] = L[k], L[r]
            r = k
    return L


# 기수 정렬
def RadixSort(L):
    radix, modulus, div = 10, 10, 1
    #nordx = getrdx(L, modulus)
    maxi = 0
    for val in L:
        digit = 0
        while val > 0:
            digit += 1
            val //= modulus
        if (digit > maxi):
            maxi = digit
    nordx = maxi
    for i in range(nordx):
        buckets = [[] for i in range(radix)]
        for value in L:
            buckets[(value % modulus) // div].append(value)
        modulus, div = modulus * 10, div * 10
        L = []
        for x in buckets:
            L.extend(x)
    return(L)


# 리스트 정렬 체크
def check(L1, L2):
    L1 = sorted(L1)
    if (L1 == L2):
        print("정렬이 올바르게 수행됨\n")
    else:
        print("정렬이 올바르게 수행되지 않음\n")


# 리스트 생성
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []
L6 = []
for i in range(2000):
    a = random.randint(0, 100000)
    L1.append(a)
    L2.append(a)
    L3.append(a)
    L4.append(a)
    L5.append(a)
    L6.append(a)

# 정렬 수행 및 결과 확인

print("버블 정렬 수행")
#print("정렬 전:", L1)
bubble = BubbleSort(L1)
#print("정렬 후:", bubble)
check(L1, bubble)

print("선택 정렬 수행")
print("정렬 전:", L2)
selection = SelectionSort(L2)
print("정렬 후:",selection)
check(L2, selection)

print("삽입 정렬 수행")
print("정렬 전:", L3)
insertion = InsertionSort(L3)
print("정렬 후:",insertion)
check(L2, insertion)

print("쉘 정렬 수행")
print("정렬 전:", L4)
shell = ShellSort(L4)
print("정렬 후:",shell)
check(L4, shell)

print("힙 정렬 수행")
print("정렬 전:", L5)
heap = HeapSort(L5)
print("정렬 후:",heap)
check(L5, heap)

print("기수 정렬 수행")
print("정렬 전:", L6)
radix = RadixSort(L6)
print("정렬 후:",radix)
check(L6, radix)