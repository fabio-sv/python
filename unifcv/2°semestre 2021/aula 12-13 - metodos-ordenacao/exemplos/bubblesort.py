def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])

def main():
    array = [0, 2, 4, 6, 1, 3]
    print("Arranjo original: ")
    print(array)
    print('\n')

    bubble_sort(array)
    
    print("Arranjo ordenado: ")
    print(array)

main()