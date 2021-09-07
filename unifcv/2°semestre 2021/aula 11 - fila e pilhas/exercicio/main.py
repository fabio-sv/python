from cliente import Cliente
from caixa import Caixa

if __name__ == '__main__':
    
    cliente1 = Cliente("João", 19)
    cliente2 = Cliente("Maria", 20)
    cliente3 = Cliente("Thiago", 22)

    caixa1 = Caixa(1, True, [])
    caixa2 = Caixa(2, True, [])
    
    caixa1.enfileira_cliente(cliente1)
    caixa1.enfileira_cliente(cliente2)

    caixa1.atende_cliente()

    
    caixa1.to_string()