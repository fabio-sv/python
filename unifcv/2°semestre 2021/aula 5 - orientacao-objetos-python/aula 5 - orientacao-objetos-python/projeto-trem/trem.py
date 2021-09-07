class Trem: # declaracao de classes
    
    # __init__ é um método especial utilizado como construtor da classe (inicializa o objeto).
    # Todo método de instância tem como primeiro parâmetro a própria instância. Esse argumento é chamado de self.
    # Note que os atributos não foram declarados. Isso não é necessário, pois Python é uma linguagem dinâmica.
    def __init__ (self, passageiros, max_pas):
        self._passageiros = passageiros
        self._max_pas     = max_pas
    
    def pick(self, passageiro):
        if self._max_pas > len(self._passageiros):
            self._passageiros.append(passageiro)
            
        else:
            print('O trem está cheio')
    
    def picks(self, passageiros):
        if len(passageiros) + len(self._passageiros) <= self._max_pas:
            self._passageiros.extend(passageiros)
        else:
            print('Quantidade de passageiros excede a lotação máxima. Nenhum passageiro embarcou!')
    
    def drop(self, passageiro):
        self._passageiros.remove(passageiro)
    
    def drops(self, passageiros):
        for passag in passageiros:
            self._passageiros.remove(passag)
    
    def get_qtde_passageiros(self):
        return len(self._passageiros)
    
    def get_max_pas(self):
        return self._max_pas
    
    # Utilizado para printar os objetos
    def to_string(self):
        print('### Trem ### nº de pass: ' + str(len(self._passageiros)))
        print('nº max: ' + str(self._max_pas))
        print('Lista de passageiros: ')

        for passag in self._passageiros:
            passag.to_string()


'''
* __new__ é o verdadeiro construtor da classe e é executado antes do __init__.

* Objetos são passados por referência.

ENCAPSULAMENTO

1. Em Python não existem modficadores de acesso (private por exemplo). Os programadores usam como padrão '_atributo' para identifcar que 
um atributo deve ser tratado como private.

2. Atributos com o prefixo __ são utilizados para renomear o atributo e assim 'desfigura-lo'. Dessa maneira fica difícil acessa-lo de outra classe.
    '__nome_do_atributo' -> _nomeda_Classe\_nome_do_atributo
    Exemplo:
        __idade -> _Pessoa__idade
'''