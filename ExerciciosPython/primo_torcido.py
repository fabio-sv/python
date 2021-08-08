def primo_check(value): 
	if value == 0 or value == 1:
		return False
	else:	
		aux = True
		for i in range(2, value):
			if value % i == 0 and i != 1:
				return False
				aux = False
				break
			elif aux == True and i == value - 1:
				return True	

def primo_check_Name(value):
	if value > 9:
		reverter = list(reversed(str(value)))
		number = int("".join(reverter))	
		return primo_check(number)
	else:
		primo_check(value)	
	


value = 

if primo_check_Name(int(value)) == True:
	print("O número", value, "invertido é um número primo")
if primo_check_Name(int(value)) == False:
		print("O número", value, "invertido não é um número primo")
