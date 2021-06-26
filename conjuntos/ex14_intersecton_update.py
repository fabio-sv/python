#Mantenha os itens existentes em ambos os conjuntos e definidos:`x``y`

x = {"apple", "banana", "chery"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#{'apple'}