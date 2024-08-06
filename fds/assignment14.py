

def bubbleSort(l):
    leng = len(l)

    for i in range(leng-1):
        for j in range(0, leng-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return j


test = [5,2,5,6,7,1,3,6,0]

print(test)
bubbleSort(test)
print(test)
