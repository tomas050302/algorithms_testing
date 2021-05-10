sorted = []


def get_min(arr):
    min = arr[0]
    min_index = 0

    for i in range(len(arr)):
        if(arr[i] < min):
            min = arr[i]
            min_index = i

    return min, min_index


def selection_sort(arr, i):
    if(i == len(arr)-1):
        return arr

    min, min_index = get_min(arr[i:])

    arr[i], arr[min_index] = min, arr[i]

    return selection_sort(arr, i+1)


arr = [2, 4, 7, 8, 2, 3, 5, 56, 8, 9, 1, 1, 9]

print(selection_sort(arr, 0))
