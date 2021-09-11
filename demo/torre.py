class Torre:
    def __init__(self, numero):
        self._numero = numero
        self._discos = []

    def esta_vazia(self):
        return self._discos == [] 

    def empilha(self, discos):
        self._discos.insert(0, discos)

    def desempilha(self):
        self._discos.pop(0)

    def first(self):
        return self.discos[0]             

    def toString(self):
        print("Torre:", str(self._numero)) 

        for disco in self._discos:
            disco.to_string()     