from trem       import Trem
from estacao    import Estacao
from passageiro import Passageiro
from log        import Log

def print_estado(trem, estacoes):
    trem.to_string()

    for estacao in estacoes:
        estacao.to_string()


'''
Parâmetros open
'r' Leitura
'w' Escrita. Substitui o conteúdo existente - cria o arquivo caso não exista
'x' Escrita. Retorna um erro caso o arquivo já exista
'a' Escrita. Insere os novos dados no final do arquivo - cria o arquivo caso não exista
'b' Modo binário
't' Modo texto - default
'+' Atualizar. Tanto leitura quanto escrita
'''

def load_passageiros():
    passageiros = []
    
    # abertura e leitura de um arquivo
    arquivo = open('loading-passageiros.txt', 'r')

    # um arquivo pode ser interpretado como uma lista de linhas
    for linha in arquivo:
        
        #split dos dados por linha
        nome, idade = linha.split(',')
        
        passageiro = Passageiro(nome, idade)
        passageiros.append(passageiro)

    arquivo.close()
    return passageiros

def load_estacoes():
    estacoes = []
    
    arquivo = open('loading-estacoes.txt', 'r')
    for linha in arquivo:
        num, nome, _, trem = linha.split(',')
        estacao = Estacao(num, nome, [], trem)
        estacoes.append(estacao)

    arquivo.close()
    return estacoes

if __name__ == '__main__':
    
    #inicializacao
    log = Log()
    
    trem = Trem([], 10)
    log.write_log('Trem inicializado')
    '''
    for passageiro in load_passageiros():
        passageiro.to_string()
    
    for estacao in load_estacoes():
        estacao.to_string()
    '''

    passageiros = load_passageiros()
    estacoes    = load_estacoes()
     
    estacoes[0].chegadas([passageiros[0], passageiros[1], passageiros[2], passageiros[3]])
    estacoes[1].chegadas([passageiros[4], passageiros[5], passageiros[6], passageiros[7]])
    estacoes[2].chegadas([passageiros[8], passageiros[9], passageiros[10]])
    # fim da inicializacao

    #estacao A -> trem
    estacoes[0].ups_trem([passageiros[0], passageiros[1], passageiros[2]], trem)
    
    #muda trem de estacao
    estacoes[0].set_trem(False)
    estacoes[1].set_trem(True)
    
    #trem -> estacao B
    estacoes[1].downs_trem([passageiros[0], passageiros[1], passageiros[2]], trem)
    estacoes[1].ups_trem([passageiros[5], passageiros[6]], trem)
    
    #muda trem de estacao
    estacoes[1].set_trem(False)
    estacoes[2].set_trem(True)

    #estacao C -> trem
    estacoes[2].ups_trem([passageiros[9], passageiros[10]], trem)
    
    print_estado(trem, estacoes)
