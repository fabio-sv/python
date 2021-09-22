# abrir arquivo para leitura
f = open("demoArquivo.txt")

#Ler - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existe
f = open("demoArquivo.txt", "r") 

#escreve um texto no arquivo
def escreve_log(self, texto):
    arquivo = open("demoArquivo.txt", "a+")

    arquivo.write(texto + "\n")

    arquivo.close()



