from functools import reduce

# reduce não é uma função embutida do Python

def soma(a, b):
    return a + b

if __name__ == '__main__':
    valor = reduce(soma, range(5))

    #aplicação de funções anônimas
    #valor = reduce(lambda a,b: a + b, range(5))

    print(list(range(5)))
    print(valor)
