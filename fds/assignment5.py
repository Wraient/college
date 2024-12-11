

def bubbleSort(l):
    leng = len(l)

    for i in range(leng-1):
        for j in range(0, leng-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l


def selectionSort(l):

    leng = len(l)

    for i in range(leng):
        min_idx = i
        for j in range(i+1, leng):
            if l[min_idx] > l[j]:
                min_idx = j

        l[min_idx], l[i] = l[i], l[min_idx]

    return l


test = [5,2,5,6,7,1,3,6,0]

print(test)
# print(bubbleSort(test))
print(selectionSort(test))
# print(test)
