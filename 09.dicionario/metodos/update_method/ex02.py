#Insira um item no dicionário
carro = {
	"Marca": "Ford",
	"Modelo": "Mustang",
	"Ano": 2021
}
carro.update({"Cor": "Branco"})

print(carro)
#{'Marca': 'Ford', 'Modelo': 'Mustang', 'Ano': 2021, 'Cor': 'Branco'}