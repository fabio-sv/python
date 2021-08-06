import json

x = {
    "nome": "Joe",
    "idade": "20",
    "cidade": "Nova York"
}

#converte para JSON
y = json.dumps(x)
print(y)

#{"nome": "Joe", "idade": "20", "cidade": "Nova York"}