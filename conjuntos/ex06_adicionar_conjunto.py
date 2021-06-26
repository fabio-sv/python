#Adicione elementos de :`motos` em ` carros`
motos = {"Z1000", "XJ6", "Hornet"}
carros = {"Jetta", "Cruze", "Golf"}

carros.update(motos)

print(carros)

#{'Jetta', 'Hornet', 'Cruze', 'Golf', 'Z1000', 'XJ6'}