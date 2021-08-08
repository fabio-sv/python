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

for number in range(0, 100):
	if primo_check(number):
		print(number, "p")
	elif primo_check(number) == False:
		print(number)	
