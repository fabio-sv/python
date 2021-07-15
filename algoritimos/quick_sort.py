import random

arr = [3, 2, 1, 4, -1, 20, -80]


def my_quick_sort (arr):
  low = 0 
  high = len(arr) -1
  threshold = arr[low]


  if low > high:
    return

  while low < high:
    while low < high and arr[high] > threshold:
        high = high - 1

    if low < high:
        arr[low] = arr[high]    

    while low < high and arr[high] <= threshold:
      low = low + 1

    if low < high:
        arr[high - 1] = arr[i]

    arr[low] = threshold   

my_quick_sort(arr)

print(arr)




 

