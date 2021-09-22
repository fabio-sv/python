from functools import reduce

def soma(a, b):
    return a + b

if __name__ == '__main__':
    valor = reduce(soma, range(5))    

    print(list(range(5)))
    print(valor)