class Cliente:
     def __init__(self, nome, idade):
         self._nome     = nome
         self._idade    = idade

     def to_string(self):
         print('Cliente: ' + self._nome + " idade: " + str(self._idade))