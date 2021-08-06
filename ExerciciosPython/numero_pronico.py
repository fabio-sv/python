#Um número é considerado número prônico se for o produto de dois números consecutivos.
numero = 90
for i in range(1, 10):
	aux = False
	if i * (i + 1) == int(numero):
		print(numero, "é prônico")
		break	
	if(i == 9):
		print(numero, "não é prônico")