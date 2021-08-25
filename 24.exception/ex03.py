try:
	print(x)
except NameError:
	print("erro NameError")
finally:
	print("esse bloco sempre será executado")		