def fatorial(valor):
    return 1 if valor < 2 else valor * fatorial(valor - 1)

if __name__ == '__main__':
    fac = fatorial
    fac(5)

    lista = list(map(fac, range(5)))
    print(lista) 

    # Comprehension
    lista2 = [fac(valor) for valor in range(5)]
    print(lista) 

