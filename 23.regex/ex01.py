import re

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
x = re.search("^Lorem.*elit$", txt)

if x:
    print("Sim")
else:
    print("Não")    

#Sim    