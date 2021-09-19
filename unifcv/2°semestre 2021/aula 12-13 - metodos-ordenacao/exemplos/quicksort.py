def partition(arr, p, r):
    x = arr[r]
    print('pivo: ', str(x))
    print('arr inicio: ', arr[p:r+1])
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    print('arr fim: ', arr[p:r+1], '\n')
    return i + 1

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)
       
def main():
    array = [5, 2, 4, 6, 1, 3]
    print("Arranjo original: ")
    print(array)
    print('\n')

    quick_sort(array, 0, len(array) - 1)
    
    print("Arranjo ordenado: ")
    print(array)

main()