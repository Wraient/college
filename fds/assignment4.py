
def binary_search(l, target):
    start = 0
    end = len(l)

    while start<end:
        mid = (start + end)//2
        if l[mid] > target:
            # start = mid+1
            end = mid
        elif l[mid] < target:
            # end = mid
            start = mid
        elif l[mid] == target:
            return mid

    return -1


stdCount = int(input("Enter the number of student: "))

list1 = {}
for i in range(stdCount):
    name, num = input("Enter the number and name of the student seprated by command (Student,Number): ").split(",")
    print("Name:", name)
    print("Num:", num)
    list1[int(num)] = name

list1 = list(list1.keys())
list1.sort()
print(list1)

target = input("Enter the Number you want to find: ")
# list1 = [1,2,3,4,5,6,7,11]
# target = 2
index = binary_search(list1, int(target))
print(index)

if index<0:
    print(f"{target} was not found in {list1}")
else:
    print(f"{target} is found at index {index}\nin list {list1}")
    print("Target was found")


