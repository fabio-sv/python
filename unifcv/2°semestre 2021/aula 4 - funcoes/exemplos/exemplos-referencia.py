''' 
# valor
def func_valor(a, b, c):
	c = a + b
	print('c1: ', c)
	
def main():
	a = 2
	b = 3
	c = 0
	func_valor(a, b, c)
	print('c2: ', c)
'''


'''
# referência
def func_ref(lista):
	lista.append(2)
	print(lista)
	
def main():
	lista_aux = []
	lista_aux.append(1)
	func_ref(lista_aux)
	print(lista_aux)
'''

'''
def magia(a, b, c):
	return a + b, b + c

def main():
	a = 1
	b = 2
	c = 3
	#x, y = magia(a, b, c)
	#print(x, y)
	
	x, _ = magia(a, b, c)
	print(x)
'''

main()