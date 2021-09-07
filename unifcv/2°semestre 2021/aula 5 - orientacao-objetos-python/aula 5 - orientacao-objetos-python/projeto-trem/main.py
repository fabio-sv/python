from trem       import Trem
from estacao    import Estacao
from passageiro import Passageiro

def print_estado(trem, estacoes):
    trem.to_string()

    for estacao in estacoes:
        estacao.to_string()

if __name__ == '__main__':
    
    #inicializacao
    trem = Trem([], 10)
    
    pass1 = Passageiro('Fernando'  , 27)
    pass2 = Passageiro('Vinicius'  , 28)
    pass3 = Passageiro('Gildo'     , 28)
    pass4 = Passageiro('Alessandro', 25)
    pass5 = Passageiro('Higor'     , 24)
    pass6 = Passageiro('Clara'     , 24)
    pass7 = Passageiro('Enrique'   , 23)
    pass8 = Passageiro('Yuri'      , 25)
    pass9 = Passageiro('Fabio'     , 27)
    pass10 = Passageiro('Marcel'    , 29)
    pass11 = Passageiro('Danilo'    , 26)
    
    estacao_a = Estacao(1, 'A', [], True)
    estacao_b = Estacao(2, 'B', [], False)
    estacao_c = Estacao(3, 'C', [], False)

    estacao_a.chegadas([pass1, pass2, pass3, pass4])
    estacao_b.chegadas([pass5, pass6, pass7, pass8])
    estacao_c.chegadas([pass9, pass10, pass11])
    
    estacoes = []
    estacoes.extend([estacao_a, estacao_b, estacao_c])
    # fim da inicializacao

    #estacao A -> trem
    estacao_a.ups_trem([pass1, pass2, pass3], trem)
    
    #muda trem de estacao
    estacao_a.set_trem(False)
    estacao_b.set_trem(True)
    
    #trem -> estacao B
    estacao_b.downs_trem([pass1, pass2, pass3], trem)
    estacao_b.ups_trem([pass6, pass7], trem)
    print_estado(trem, estacoes)

    #muda trem de estacao
    estacao_b.set_trem(False)
    estacao_c.set_trem(True)

    #estacao C -> trem
    estacao_c.ups_trem([pass9, pass10], trem)
    print_estado(trem, estacoes)
    
