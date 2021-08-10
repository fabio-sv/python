try:
	arquivo = open("exemplo.file.txt")
	arquivo.write("Escrever no arquivo")
except:
	print("erro")
finally:
	arquivo.close()
	print("finaliza o processo")		
	
			