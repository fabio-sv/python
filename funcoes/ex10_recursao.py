def my_recursion(k):
  if (k > 0):
    result = k + my_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

my_recursion(6)