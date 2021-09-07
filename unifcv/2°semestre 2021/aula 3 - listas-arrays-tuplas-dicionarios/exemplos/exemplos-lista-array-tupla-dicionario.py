from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

print(floats[-1])

dicionario = {
    'nome' : 'João da Silva',
    'idade': 24,
    'rg'   : '541561111',
    'cpf'  : '09877701947'
}

#print(dicionario.nome) não funciona porque dicionario não é um objeto
print(dicionario['nome'])