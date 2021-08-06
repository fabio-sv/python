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

print(json.dumps(x, indent=2, sort_keys=True))

'''
{
  "carros": [
    {        
      "modelo": "Camaro",
      "placa": "afc12h38"
    },
    {
      "modelo": "Mustang",
      "placa": "adc73f24"
    }
  ],
  "casado": true,
  "divorciado": false,
  "filhos": [
    "Ana",
    "Bob"
  ],
  "idade": 39,
  "nome": "Joe",
  "pets": null
}
'''