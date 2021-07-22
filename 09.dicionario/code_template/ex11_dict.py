carro = {
    "marca": "Ferrari",
    "modelo": "Monza",
    "ano": 2020
}

x = carro.keys()

print(x)

#dict_keys(['marca', 'modelo', 'ano'])

carro["cor"] = "Vermelho"

print(x)

#dict_keys(['marca', 'modelo', 'ano', 'cor'])