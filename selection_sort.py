import random


def get_min(arr, start_index):
    min = arr[start_index]
    min_index = start_index

    for i in range(start_index, len(arr)):
        if(arr[i] < min):
            min = arr[i]
            min_index = i

    return min, min_index


def selection_sort(arr, i=0):
    if(i == len(arr)-1):
        return arr

    min, min_index = get_min(arr, i)

    arr[i], arr[min_index] = min, arr[i]

    return selection_sort(arr, i+1)


print('\n\n--- Best Case ---\n')  # O(n^2)

arr = []
for i in range(500):
    arr.append(i)

print(selection_sort(arr))

print('\n\n--- Averege Case ---\n')  # O(n^2)
arr = []
for i in range(500):
    arr.append(random.randint(1, 500))

print(selection_sort(arr))

print('\n\n--- Worst Case ---\n')  # O(n^2)
arr = []
for i in range(500):
    arr.append(500-i)

print(selection_sort(arr))
