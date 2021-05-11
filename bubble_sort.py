import random


def bubble_sort_optimized(arr):
    sorted = False
    for _ in range(len(arr)-1):
        if(sorted):
            return arr
        sorted = True
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


def bubble_sort(arr):
    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


print('\n\n--- Best Case ---\n')  # O(n)

arr = []
for i in range(500):
    arr.append(i)

bubble_sort_optimized(arr)

print('\n\n--- Averege Case ---\n')  # O(n ^ 2)

arr = []
for i in range(500):
    arr.append(random.randint(1, 500))

bubble_sort_optimized(arr)

print('\n\n--- Worst Case ---\n')  # O(n ^ 2)

arr = []
for i in range(500):
    arr.append(500-i)

bubble_sort_optimized(arr)
