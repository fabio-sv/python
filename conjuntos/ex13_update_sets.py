#O método insere os itens no conjunto2 no conjunto1:update()

my_set1 = {"a", "b", "c"}
my_set2 = {1, 2, 3}

my_set1.update(my_set2)

print(my_set1)

#{1, 2, 3, 'a', 'b', 'c'}