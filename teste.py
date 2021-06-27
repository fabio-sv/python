N = int(input())

for i in range(0, N):
 A = input()
 B = input()

 value1 = A[-2:]
 value2 = B[-2:]

 if value1 == value2:
   print("encaixa")
 else:
   print("não encaixa") 