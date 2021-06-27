#Mantenha os itens que não estão presentes em ambos os conjuntos:

x = {"Nike", "Adidas", "Puma"}
y = {"Puma", "Vans", "Allstar"}

x.symmetric_difference_update(y)

print(x)

#{'Vans', 'Nike', 'Allstar', 'Adidas'}

