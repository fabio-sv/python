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

class Estacoes:
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

    def chegada(self, passageiros): 
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

#----------------main--------------------

if __name__ == '__main__':
  passageiro1 = Passageiro("John", 20)

  print(passageiro1.get_nome())
  print(passageiro1.get_idade())

