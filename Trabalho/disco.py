class Disco:
    def __init__(self, tamanho, cor):
        self._tamanho = tamanho
        self._cor = cor

    def getTamanho(self):
        return self._tamanho

    def getCor(self):
        return self._cor 

    def toString(self):
        for _ in range(self._tamanho):
            print("-", end=" ")

        print(" ", str(self._tamanho))               