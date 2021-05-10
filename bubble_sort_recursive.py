import time
import random


def bubble_sort(arr, i=0, count=0):
    if(i == len(arr)-1):
        for j in range(len(arr)-1):
            count += 1
            if(not (arr[j] <= arr[j+1])):
                bubble_sort(arr, j, count+1)

        print(count)
        return arr

    if(arr[i] > arr[i+1]):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp

    return bubble_sort(arr, i+1, count+1)


count = 0
arr = []

for i in range(35):
    arr.append(random.randint(1, 35))

start = time.time()

print(bubble_sort(arr))
print(count)

end = time.time()
print(f'O bubble sort demorou {end-start} segundos')
