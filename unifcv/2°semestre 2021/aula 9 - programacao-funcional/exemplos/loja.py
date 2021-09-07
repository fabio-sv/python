from functools import reduce

def adiciona_produto(carrinho, produtos):
    cod_produto = input("Digite o código do produto: ")
    carrinho.append(cod_produto)
    menu(carrinho, produtos)

def remove_produto(carrinho, produtos):
    cod_produto = input("Digite o código do produto: ")
    carrinho.remove(cod_produto)
    menu(carrinho, produtos)

def finaliza_compra(carrinho, produtos):
    valor = reduce(lambda a, b: a + b, [produtos[key] for key in carrinho])
    
    print("Valor total do pedido: "+ str(valor))

def soma(a, b):
    return a + b

def menu(carrinho, produtos):
	print('\n### Menu ###')
	tipo = int(input("Digite a operação: "))
	
	if tipo == 1:
		adiciona_produto(carrinho, produtos)
	elif tipo == 2:
		remove_produto(carrinho, produtos)
	elif tipo == 3:
		finaliza_compra(carrinho, produtos)
	else:
		print('Operação inválida')
		menu(carrinho, produtos)

if __name__ == '__main__':
    produtos = {
        '101': 5.40, 
        '105': 8.90, 
        '106': 12.00, 
        '108': 1.99, 
        '109': 0.50, 
        '110': 10.56
    }

    carrinho = []

    menu(carrinho, produtos)