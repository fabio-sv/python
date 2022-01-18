# inicialização
def initialize_single_source(grafo, s):
    for vertice in grafo:
        vertice['dist'] = float('inf') #infinito
        vertice['pai'] = None

    s['dist'] = 0    

#relaxamento
def relax(u, v, w):
    if v['dist'] > u['dist'] + w:
        v['dist'] = u['dist'] + w
        v['pai'] = u

def bellman_ford(grafo, s):
    initialize_single_source(grafo, s)

    for _ in range(0, len(grafo) - 1):
        for u in grafo:
            for adj in u['adjs']:
                relax(u, adj['vertice'], adj['peso'])

    #verificação de ciclos negativos
    for u  in grafo:
        for adj in u['adjs']:
            if adj['vertice'] ['dist'] > u['dist'] + adj['peso']:
                return False  

    return True                        

if __name__ == '__main__':
    
    # vértices
    s = { 'nome'   : 's', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    t = { 'nome'   : 't', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    y = { 'nome'   : 'y', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    x = { 'nome'   : 'x', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }
    z = { 'nome'   : 'z', 'dist'   : 0, 'pai'    : None, 'adjs'    : [] }

    s['adjs'].extend(
        [
            { 'vertice': t, 'peso': 6 },
            { 'vertice': y, 'peso': 7 }
        ]
    )
    
    t['adjs'].extend(
        [
            { 'vertice': x, 'peso': 5 },
            { 'vertice': y, 'peso': 8 },
            { 'vertice': z, 'peso': -4 },
        ]
    )

    y['adjs'].extend(
        [
            { 'vertice': x, 'peso': -3 },
            { 'vertice': z, 'peso': 9 }
        ]
    )
    x['adjs'].extend(
        [
            { 'vertice': t, 'peso': -2 }
        ]
    )

    z['adjs'].extend(
        [
            { 'vertice': s, 'peso': 2 },
            { 'vertice': x, 'peso': 7 }
        ]
    )

    grafo = [s, t, y, x, z]
    no_neg_cicle = bellman_ford(grafo, grafo[0])

    print(no_neg_cicle)
    #print do resultado final
    for vertice in grafo:
        print(vertice['nome'] + ' - ' + str(vertice['dist']), end="")
        if vertice['pai']:
            print(" - " + vertice['pai'] ['nome'])
        else:
            print()    