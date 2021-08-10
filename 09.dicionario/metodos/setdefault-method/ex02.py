#Obtenha o valor do item "cor", se o item "cor" não existir, 
#insira "cor" com o valor "branco"
carro = {
	"Marca": "Ford",
	"Modelo": "Mustang",
	"Ano": 2021
}
carro.setdefault("Cor", "Branco")

print(carro)
#{'Marca': 'Ford', 'Modelo': 'Mustang', 'Ano': 2021, 'Cor': 'Branco'}