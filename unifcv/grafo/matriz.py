def load_grafo():
	matriz = []
	vertices = {}

	arquivo = open('matriz.txt', 'r')

	count = 0
	for line in arquivo:

		if count == 0:
			vertices_aux = line.strip().split(',')

			indice = 0
			for v in vertices_aux:
				vertices[v] = indice
				indice += 1

		else:
			matriz.append(line.strip().split(' '))

		count += 1

	return vertices, matriz


def acessa_posicao(matriz, vertices, chave_l, chave_c):
    return matriz[vertices[chave_l]] [vertices[chave_c]] 

if __name__ == '__main__':
	vertices, matriz = load_grafo()
	print('Vertices:', vertices)
	print('Matriz:', matriz)
	
	print('Posição:', acessa_posicao(matriz, vertices, '1', '1'))
