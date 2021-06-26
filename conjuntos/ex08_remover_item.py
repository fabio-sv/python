#Remova a "banana" usando o método`remove()`:

my_set = {"John", "Bob", "Sara"}

my_set.remove("Sara")

print(my_set)

#{'John', 'Bob'}

my_set2 = {"banana", "maçã", "uva"}

my_set2.discard("banana")

print(my_set2)

#{'uva', 'maçã'}