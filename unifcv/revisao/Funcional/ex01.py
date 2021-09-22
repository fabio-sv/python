def par(valor):
    return valor % 2 == 0 #true / false


if __name__=='__main__':

    # filtra os valores pares de uma lista
    lista = list(filter(par, range(8)))
    print(lista)

    #list Comprehension
    lista2 = [n for n in range(8) if n % 2 == 0] 