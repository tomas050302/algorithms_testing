import random


def merge(arr1, arr2):
    i = 0
    j = 0
    arr = []

    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    while(i < len(arr1)):
        arr.append(arr1[i])
        i += 1

    while(j < len(arr2)):
        arr.append(arr2[j])
        j += 1

    return arr


def sort(arr):
    if(len(arr) <= 1):
        return arr

    mid = len(arr)//2

    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


print('\n\n--- Best Case ---\n')  # O(n log(n))

arr = []
for i in range(500):
    arr.append(i)

print(sort(arr))

print('\n\n--- Averege Case ---\n')  # O(n log(n)

arr = []
for i in range(500):
    arr.append(random.randint(1, 500))

print(sort(arr))

print('\n\n--- Worst Case ---\n')  # O(n log(n)

arr = []
for i in range(500):
    arr.append(500-i)

print(sort(arr))
