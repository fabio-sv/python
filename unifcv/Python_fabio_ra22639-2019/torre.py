class Torre:
    def __init__(self, numero):
        self.numero = numero
        self._discos = []

    def esta_vazia(self):
        return self._discos == []

    def empilha(self, disco):
        self._discos.insert(0, disco)

    def desempilha(self):
        return self._discos.pop(0)

    def first(self):
        return self._discos[0]

    def to_string(self):
        print('\nTorre:', str(self._numero))

        for disco in  self._discos:
            disco.to_string()                    