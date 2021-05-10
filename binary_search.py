import time


def binary_search(arr, n, left, right):
    mid = (left + right) // 2

    if(arr[mid] == n):
        return mid

    if(len(arr) == 1):
        return -1

    if(arr[mid] > n):
        return binary_search(arr, n, left, mid-1)
    else:
        return binary_search(arr, n, mid+1, right)


def sequencial_search(arr, n):
    for item in arr:
        if(item == n):
            return item


arr = []

length = int(input('Quantos valores pretende que o array tenha: '))

for i in range(length):
    arr.append(i)

n = int(input('Introduza o valor a procurar: '))

start = time.time()
index = binary_search(arr, n, 0, len(arr))
end = time.time()

print(f'O valor encontra-se na {index} posição.')
print(f'A procura binária demorou {end-start} segundos')

start = time.time()
index = sequencial_search(arr, n)
end = time.time()

print(f'O valor encontra-se na {index} posição.')
print(f'A procura sequencial demorou {end-start} segundos')
