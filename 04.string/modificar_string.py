txt  = "Hello, World";
print(txt.upper()); #HELLO, WORLD

txt2 = "HELLO, WORLD";
print(txt.lower()); #hello, world

#O método remove qualquer espaço branco desde o início ou o fim:strip()
print(txt.strip());

#O método substitui uma sequência por outra string:replace()
txt3 =  "Ola, Mundo!";
print(txt3.replace("O", "A")); #Ala, Mundo!

#O método divide a sequência em substrings se encontrar instâncias do separador:split()
print(txt3.split(",")); #['Ola', ' Mundo!']