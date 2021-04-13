def mergeSort(list):
    if len(list) <= 1:
        return list

    k = len(list) // 2
    list1 = mergeSort(list[:k])
    list2 = mergeSort(list[k:])
    result = []

    while len(list1) > 0 or len(list2) > 0:
        if len(list1) > 0 and len(list2) > 0:
            elist1 = list1.pop(0)
            elist2 = list2.pop(0)
            if elist1 < elist2:
                result.append(elist1)
                list2.insert(0, elist2)
            else:
                result.append(elist2)
                list1.insert(0, elist1)
        elif len(list1) > 0:
            result.append(list1.pop(0))
        elif len(list2) > 0:
            result.append(list2.pop(0))

    return result

alist = [4, 26, 9, 3, 1, 72, 566, 43]
blist = mergeSort(alist)
print(blist)