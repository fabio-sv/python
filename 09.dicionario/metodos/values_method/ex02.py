#Quando um valor é alterado no dicionáio, o objeto de
#exibição também é alterado.
carro = {
	"Marca": "Ford",
	"Modelo": "Mustang",
	"Ano": 2021
}
x = carro.values()

carro["Ano"] = 2022

print(x)
#dict_values(['Ford', 'Mustang', 2022])