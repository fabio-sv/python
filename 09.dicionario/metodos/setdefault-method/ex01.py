#Obtenha o valor do item "Modelo"
carro = {
	"Marca": "Ford",
	"Modelo": "Mustang", 
	"Ano": 2021
}
x = carro.setdefault("Modelo")

print(x)
#Mustang