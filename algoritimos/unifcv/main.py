from fila import Fila
from pilha import Pilha

if __name__ == '__main__':

    pilha = Pilha()

    pilha.adiciona(1)
    pilha.adiciona(2)
    pilha.adiciona(3)

    pilha.to_string()

    print("Remove: ", pilha.remove())
    print("Proximo: ", pilha.how_is_next())

    fila = Fila()

    fila.inp(1)
    fila.inp(2)
    fila.inp(3)

    fila.to_string()
    print("Remove: ", fila.remove())

