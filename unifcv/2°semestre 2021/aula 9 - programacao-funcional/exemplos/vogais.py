def vogal(letra):
    letras_vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return 1 if letra in letras_vogais else 0

def count_vogais(texto):
    lista = list(filter(vogal, texto))
    print(lista)
    return len(lista)

if __name__ == '__main__':
    texto = 'quantasvogaistemnessetexto'
    print(count_vogais(texto))