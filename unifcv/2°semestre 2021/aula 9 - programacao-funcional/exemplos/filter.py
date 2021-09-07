def par(n):
    return n % 2 == 0

if __name__ == '__main__':

    lista = list(filter(par, range(8)))
    print(lista)

    # List Comprehension
    lista2 = [n for n in range(8) if n % 2 == 0]
    print(lista2)