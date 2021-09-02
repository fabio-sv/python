class Passageiro:
  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade

  def get_nome(self):
    return self._nome 

  def set_nome(self, nome):
    self._nome = nome  

  def get_idade(self):
    return self._idade

  def set_idade(self, idade):
    self._idade = idade    
    
  def to_string(self):
    print(self._nome, str(self._idade))  
#---------------------------------------
class Trem:
  def __init__(self, pessoas, max_pas):
    self._pessoas = pessoas
    self._max_pas = max_pas

  def pick(self, passageiro):
    if self._max_pas > len(self._passageiros):
      self._passageiros.append(passageiro)  

  def picks(self, passageiros):  
    if self._max_pas > len(self._passageiros) + len(passageiros):
      self._passageiros.extend(passageiros)  

  def drop(self, passageiro):
    self._passageiros.remove(passageiro)  

  def drops(self, passageiros):
    for passag in passageiros:
      self._passageiros.remove(passag)  

  def get_qtde_passageiro(self):
    return len(self._passageiros)  

  def get_max_pas(self):
      return self._max_pas

  def to_string(self):
      print("### Trem ### n° de pessoas", str(len(self._passageiros)))

      print("n° max:", str(self._max_pas))

      print("Lista de passageiros")
      for passag in self._passageiros:
          passag.to_string()    
#---------------------------------------
class Estacao:
    def __init__(self, nome, numero_estacao, passageiro, trem):
     self._nome = nome
     self._numero_estacao = numero_estacao
     self._passageiro = passageiro
     self._trem = trem;

    def get_num(self):
        return self._num 

    def set_num(self, num):
        self._num = num  

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome    

    def get_trem(self):
        return self._trem

    def set_trem(self, trem):
        self._trem = trem  

    def chegada(self, passageiro): 
        self._passageiros.append(passageiro)        

    def chegadas(self, passageiros): 
        self._passageiros.extend(passageiros) 

    def saida(self, passageiro): 
        self._passageiros.remove(passageiro)     

    def saida(self, passageiros):
        for passag in passageiros:
            self._passageiros.remove(passag)

    def up_trem(self, passageiro, trem):
        if self._trem:
            trem.picks(passageiro)
            self._passageiros.remove(passageiro)

    def ups_trem(self, passageiro, trem):
        if self._trem:
            trem.picks(passageiro)
            for passag in self._passageiros:
                self._passageiros.remove(passag)

    def down_trem(self, passageiro, trem):
        if self._trem:
            self._passageiros.append(passageiro)
            trem.drop(passageiro)  

    def downs_trem(self, passageiros, trem):
        self._passageiros.extend(passageiros)
        trem.drops(passageiros)

    def to_string(self):
        print("\n ### Estação:", str(self._num, "-" , self._nome))

        print("Trem:", str(self._trem))
        print("Lista de passageiros:")

        for passag in self._passageiros:
            passag.to_string()                          
#------------------------------------
def print_estacao(trem, estacoes):
  trem.to_string
  for estacao in estacoes:
    estacao.to_string()

if __name__ == '__main__':

  trem = Trem([], 10)

  passageiro1 = Passageiro("John", 20)
  passageiro2 = Passageiro("Jane", 30)
  passageiro3 = Passageiro("Joe", 25)
  passageiro4 = Passageiro("Tommy", 32)
  passageiro5 = Passageiro("Tom", 62)
  

  estacao_a = Estacao("Oxford", 1, [], True)
  estacao_b = Estacao("Londres", 2, [], False)
  estacao_c = Estacao("Manchester", 3, [], False)

  estacao_a.chegadas([passageiro1, passageiro2, passageiro3])
  estacao_b.chegadas([passageiro4])
  estacao_c.chegadas([passageiro5])

  estacoes = []
  estacoes.extend([estacao_a, estacao_b], estacao_c)

  estacao_a.ups_trem([passageiro1, passageiro2, passageiro3], trem)
  estacao_a.set_trem(False)
  estacao_b.set_trem(True)

  estacao_b.down_trem(passageiro3, trem)
  estacao_b.up_trem(passageiro4, trem)

  print_estacao(trem, estacoes)


