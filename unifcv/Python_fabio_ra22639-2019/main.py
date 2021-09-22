from torre import Torre
from disco import Disco
from config import Config

def move_op(torre1, torre2):
    torre2.empilha(torre1.first())
    torre1.desempilha()

def move(torre1, torre2):
    if torre2.esta_vazia():
        move_op(torre1, torre2)
        return True

    elif torre1.esta_vazia():
        print('A torre de origem não tem mais elementos.')
        return False

    elif torre1.first().get_tamanho < torre2.first().get_tamanho():
        move_op(torre1, torre2)
        return True

    else:
        print('Opção não permitida.')
        return False

def menu(torres, config):
    print('\n### Menu ###')
    print('#1 - movimento')
    print('#2 - finalizar\n')
    opcao =  int(input('Opção: '))

    if(opcao == 1):
        t1 = int(input('Torre origem: '))
        t2 = int(input('Torre destino: '))
        ver = move(torres[t1], torres[t2])
        if ver:
            config.status_torres(torres)

        menu(torres, config)

    elif(opcao == 2):
        config.status_torres(torres)   

if __name__=='__main__':
    print('### Torre de Hanói ###\n')

    torres = []
    torres.extend([Torre(1), Torre(2),  Torre(3)])

    config = Config()
    config.init_discos(torres[0])
    config.status_torres(torres)

    menu(torres, config)             
 