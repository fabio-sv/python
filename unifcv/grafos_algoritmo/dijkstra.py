# http://dontpad.com/asdfasdfasdfhaslkfajhsdfaskldifhads

from functools import reduce

# inicialização de todos os vertices do grafo
def initialize_single_source(grafo, s):
    for vertice in grafo:
        vertice['dist'] = float('inf') # definição de inteiro positivo infinito
        vertice['pai']  = None
    
    s['dist'] = 0 # vértice de origem tem distância 0

# processo de relaxamento
def relax(u, v, w):
    if v['dist'] > u['dist'] + w:
        v['dist'] = u['dist'] + w
        v['pai']  = u  

# recupera o elemento com menor distância em relação a origem
def extract_min(fila):
    return fila.pop(
        fila.index(
            reduce(lambda el1, el2: el1 if el1['dist'] < el2['dist'] else el2, fila)))

def dijkstra(grafo, s):
    initialize_single_source(grafo, s)
    
    # conjunto de vértices já finalizados
    S = []
    
    # fila de prioridade
    fila = []
    fila.extend(grafo)

    while(fila != []):
        u = extract_min(fila)
        S.append(u['nome'])

        print(u['nome'])
        
        for adj in u['adjs']:
            relax(u, adj['vertice'], adj['peso'])
        
    
    print(S)
        
if __name__ == '__main__':
    
    # vértices
    s = { 'nome'   : 's', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    t = { 'nome'   : 't', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    y = { 'nome'   : 'y', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    x = { 'nome'   : 'x', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    z = { 'nome'   : 'z', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    
    s['adjs'].extend(
        [
            { 'vertice': t, 'peso': 10 },
            { 'vertice': y, 'peso': 5  }
        ]
    )
    
    t['adjs'].extend(
        [
            { 'vertice': x, 'peso': 1 },
            { 'vertice': y, 'peso': 2 }
        ]
    )

    y['adjs'].extend(
        [
            { 'vertice': t, 'peso': 3 },
            { 'vertice': x, 'peso': 9 },
            { 'vertice': z, 'peso': 2 }
        ]
    )

    x['adjs'].extend(
        [
            { 'vertice': z, 'peso': 4 }
        ]
    )

    z['adjs'].extend(
        [
            { 'vertice': s, 'peso': 7 },
            { 'vertice': x, 'peso': 6 }
        ]
    )

    # grafo representado como uma lista de adjacência
    grafo = [s, t, y, x, z]
    dijkstra(grafo, grafo[0])