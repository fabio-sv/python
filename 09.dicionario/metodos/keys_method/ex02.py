#Quando um item é adicionado no dicionário, o objeto de exibição também é atualizado
carro = {
	"Marca": "Ford", 
	"Modelo": "Mustang",
	"Ano": 2021
}
x = carro.keys()
carro["Cor"] = "Vermelho"

print(x)
#dict_keys(['Marca', 'Modelo', 'Ano', 'Cor'])