#Remove "Modelo" do dicionário
carro = {
	"Marca": "Ford",
	"Modelo": "Mustang",
	"Ano": 2021
}
carro.pop("Modelo")

print(carro) 
#{'Marca': 'Ford', 'Ano': 2021}