import time


def bubble_sort_optimized(arr):
    sorted = False
    for j in range(len(arr)-1):
        if(sorted):
            return arr
        sorted = True
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


arr = []

for i in range(10000):
    arr.append(10000-i)  # Worst case

start = time.time()
bubble_sort_optimized(arr)

end = time.time()
print(f'O bubble sort otimizado demorou {end-start} segundos')

''' start = time.time()

bubble_sort(arr)

end = time.time()
print(f'O bubble sort não otimizado demorou {end-start} segundos')
 '''
