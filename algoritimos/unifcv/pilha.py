class Pilha:
    def __init__(self):
        #__ significa privado
        self.__itens = []

    def esta_vazia(self):
        return len(self.__itens) == 0

    def adiciona(self, item):
        self.__itens.append(item)

    def remove(self):
         return self.__itens.pop()

    def get_tamaho(self):
        return len(self.__itens)     

    def how_is_next(self):
        return self.__itens[len(self.__itens) - 1]     

    def to_string(self):
        print("Quantidade de elementos", str(self.get_tamaho()))
        for item in self.__itens:
            print(item)

