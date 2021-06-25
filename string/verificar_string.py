#Para verificar se uma determinada frase ou caractere está presente em uma sequência, podemos usar a palavra-chave in:

text  = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print("amet" in text); #true
print("into" in text); #false

#Imprimir somente se "elit" estiver presente:
if "elit" in text:
    print("Sim, elit esta no texto"); #Sim, elit esta no texto

#Para verificar se uma determinada frase ou caractere NÃO está presente em uma sequência, podemos usar a palavra-chave not in
print("ligth" not in text); #true 

#Imprimir apenas se "car" não estiver presente:
if "car" not in text:
    print("car não esta presente no texto"); #car não esta presente no texto