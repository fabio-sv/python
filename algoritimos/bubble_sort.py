import random 

#Inicia o vetor com valores aleatórios
arr = []
for i in range(0, 10):
    arr.insert(i, random.randrange(0, 100))

#Ordena o vetor - Bubbble Sort 
for i in range(0, len(arr)):
    for j in range(0, len(arr) - 1):

        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
print(arr)       
            