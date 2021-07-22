def my_function(n):
    return lambda a : a * n

dobro = my_function(2)

print(dobro(11))

#11