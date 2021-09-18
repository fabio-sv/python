from disco import Disco

class Config:
    def __init__(self):
        self._qtde_discos = int(input("Quantidade de discos: "))

    def init_discos(self, torre_inicial):
        discos = self.load_discos()

        for ix in range(self._qtde_discos):
            torre_inicial.empilha(discos[ix])

    def load_discos(self):
        discos = []
        arquivo = open('discos.txt', 'r') 

        for linha in arquivo:
            numero = linha
            discos.append(Disco(int(numero)))  

        return discos

    def get_qtde_discos(self):
        return self._qtde_discos

    def status_torres(self, torres):
        print('\n Quantidade de discos:', str(self._qtde_discos))             
              
