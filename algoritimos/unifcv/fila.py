class Fila:
    def __init__(self):
        self._itens = []

    def esta_vazia(self):
        return len(self.__itens) == 0

    def inp(self, item):
        self._itens.append(item)

    def out(self):
        return self._itens.pop(0)

    def first(self):
        return self._itens[0]

    def get_tamanho(self):
        return len(self._itens)

    def to_string(self):
        print("Quantidade de elementos:", str(self.get_tamanho()))

        for item in self._itens:
            print(item)                    
