import json 

x = {
    "nome": "Joe",
    "idade": 39,
    "casado": True,
    "divorciado": False,
    "filhos": ("Ana", "Bob"),
    "pets": None,
    "carros": [
        {"modelo": "Camaro", "placa": "afc12h38"},
        {"modelo": "Mustang", "placa": "adc73f24"}
    ] 
}

print(json.dumps(x, indent=4))

'''
{
    "nome": "Joe",
    "idade": 39,
    "casado": true,
    "divorciado": false,
    "filhos": [
        "Ana",
        "Bob"
    ],
    "pets": null,
    "carros": [
        {
            "modelo": "Camaro",
            "placa": "afc12h38"
        },
        {
            "modelo": "Mustang",
            "placa": "adc73f24"
        }
    ]
}
'''