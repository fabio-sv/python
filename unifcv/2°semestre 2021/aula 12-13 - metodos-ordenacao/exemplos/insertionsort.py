def insertion_sort(arr):
    for j in range(len(arr)):
        key = arr[j]
        i = j - 1

        while(i >= 0 and arr[i] > key):
            arr[i + 1] = arr[i]
            i -= 1
        
        arr[i + 1] = key

def main():
    array = [5, 2, 4, 6, 1, 3]
    print("Arranjo original: ")
    print(array)
    print('\n')

    insertion_sort(array)
    
    print("Arranjo ordenado: ")
    print(array)

main()