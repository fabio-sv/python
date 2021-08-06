import json 

print(json.dumps({"nome": "Joe", "idade": 29})) #{"nome": "Joe", "idade": 29}
print(json.dumps(["Volvo", "Ford"])) #["Volvo", "Ford"]
print(json.dumps(("banana", "uva"))) #["banana", "uva"]
print(json.dumps("Ola, Mundo")) #"Ola, Mundo"
print(json.dumps(120)) #120
print(json.dumps(3.18)) #3.18
print(json.dumps(True)) #true
print(json.dumps(False)) #false
print(json.dumps(None)) #null