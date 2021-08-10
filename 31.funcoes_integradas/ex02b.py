arr = [True, True, True]
print(all(arr))
#True

vet = [0, 1, 2]
print(all(vet))
#False

tupla = (0, True, False)
print(all(tupla))
#False

myset = {0, 1, 0}
print(all(myset))
#False

mydic = {0: "vermelho", 1: "branco"}
print(all(mydic))
#False 