def my_function(n):
    return lambda a : a * n

dobro = my_function(2)
triplo = my_function(3)

print(dobro(11))
print(triplo(11))

#22
#33