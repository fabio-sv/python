numero = int(input())

contador = 2
while(contador <= numero):

    if numero % contador == 0:
        print("Não primo")
        break
    else:
        print("Primo")
        break
    contador = contador + 1




