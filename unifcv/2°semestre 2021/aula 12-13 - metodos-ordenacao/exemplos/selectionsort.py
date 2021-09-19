def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        x = arr[min]
        arr[min] = arr[i]
        arr[i] = x
       
def main():
    array = [5, 2, 4, 6, 1, 3]
    print("Arranjo original: ")
    print(array)
    print('\n')

    selection_sort(array)
    
    print("Arranjo ordenado: ")
    print(array)

main()