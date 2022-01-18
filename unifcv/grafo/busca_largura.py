def busca_largura(grafo, s):
    for vertice in grafo:
        vertice['cor'] = 'branco'
        vertice['distancia'] = float('inf')  # infinito
        vertice['pai'] = None

    s['cor'] = 'cinza'
    s['distancia'] = 0
    s['pai'] = None

    #Q = 0
    #EMQUETE (Q, s)
    fila = [s]
    while(fila != []):
        u = fila.pop(0)
        print(u['nome'])

        for adj in u['adjacentes']:
            if adj['cor'] == 'branco':
                adj['cor'] = 'cinza'
                adj['distancia'] = u['distancia'] + 1
                adj['pai'] = u

                fila.append(adj)  # add vertice na fila

        u['cor'] = 'preto'


if __name__ == '__main__':
    r = {
        'nome': 'r',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    s = {
        'nome': 's',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    t = {
        'nome': 't',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    u = {
        'nome': 'u',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    v = {
        'nome': 'v',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    w = {
        'nome': 'w',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    x = {
        'nome': 'x',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }
    y = {
        'nome': 'y',
        'cor': '',
        'distancia': 0,
        'pai': None,
        'adjacentes': []
    }

    r['adjacentes'].extend([v, s])
    s['adjacentes'].extend([r, w])
    t['adjacentes'].extend([w, x, u])
    u['adjacentes'].extend([t, x, y])
    v['adjacentes'].extend([r])
    w['adjacentes'].extend([s, t, x])
    x['adjacentes'].extend([w, t, u, y])
    y['adjacentes'].extend([x, u])

# grafo representado como uma lista de adjacencia
    grafo = [s, r, t, u, v, w, x, y]
    busca_largura(grafo, grafo[0])
