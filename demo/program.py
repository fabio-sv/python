from torre import Torre
from disco import Disco
from config import Config
#import crayons

# operação from : first torre1  | to first torre2 | to first torre
def move_op(torre1, torre2):
    torre2.empilha(torre1.first())
    torre1.desempilha()

# verifica se o movimento é permitido
def move(torre1, torre2):
    if torre1.esta_vazia():
        move_op(torre1, torre2) 
        return True

    elif torre1.esta_vazia():
        print("Torre de origem não tem mais elementos.")
        return False

    elif torre1.first().getTamanho() < torre2.first().getTamanho():
        move_op(torre1, torre2)
        return True

    else:
        print("A torre de origem não tem mais elementos.")    
        return False

def menu(torres, config):
    print("\n### Menu ###")
    print("#1 - movimento")
    print("#2 - finalizar\n")
    escolha = int(input("Opção: "))

    if(escolha == 1):
        t1 = int(input("Torre origem: "))
        t2 = int(input("Torre destino: "))

        ver = move(torres[t1], torres[t2])
        if ver:
            config.status_torres(torres)
        menu(torres, config)

    elif(escolha == 2):
        config.status_torres(torres)    

# Principal
if __name__ == "__main__":
    print("### Torre de Hanói ###\n")

    torres = []
    torres.extend([Torre(1), Torre(2), Torre(3)])

    config = Config()
    config.init_discos(torres[0])
    config.status_torres(torres)

    menu(torres, config)