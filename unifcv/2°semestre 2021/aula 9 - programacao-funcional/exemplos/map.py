def fatorial(n):
    return 1 if n < 2 else n * fatorial(n - 1)

if __name__ == '__main__':
    fact = fatorial
    fact(5)

    lista = list(map(fact, range(5)))
    print(list(range(5)))
    print(lista)

    # List Comprehension
    # são mais legíveis e estão substituindo map e filter
    lista2 = [fact(n) for n in range(5)]
    print(lista2)