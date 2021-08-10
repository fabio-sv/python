#Devolve os pares de valor-chave do dicionário
carro = {
	"Marca": "Ford",
	"Madelo": "Mustang",
	"Ano": 2021
}
x = carro.items()

carro["Ano"] = 2018

print(x)
#dict_items([('Marca', 'Ford'), ('Madelo', 'Mustang'), ('Ano', 2018)])