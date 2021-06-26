#Ordena a lista 
num = [2, 6, 9, 4, -10, 11, 8];
num.sort();
print(num); #[-10, 2, 4, 6, 8, 9, 11]

#Lista decrescente 
cars = ["ford", "bmw", "volvo"];
cars.sort(reverse=True);
print(cars); #['volvo', 'ford', 'bmw']


#Classifique a lista pelo comprimento dos valores
def myFunc(valores):
    return len(valores);

cars2 = ['ford', 'vw', 'volvo', 'bmw'];
cars2.sort(key=myFunc);
print(cars2); #['vw', 'bmw', 'ford', 'volvo']

#Classifique uma lista de dicionários com base no valor "ano" dos dicionários
def myFunction(e):
    return e['year']

nomes = [
    {"nome" : "Pedro", "year" : 2005},
    {"nome" : "Mateus", "year" : 2000},
    {"nome" : "Gabriel", "year" : 2011}
    ]

nomes.sort(key=myFunction);
print(nomes); #[{'nome': 'Mateus', 'year': 2000}, {'nome': 'Pedro', 'year': 2005}, {'nome': 'Gabriel', 'year': 2011}]

#Classifique a lista pelo comprimento dos valores e inverta
def myFunction2(e):
    return len(e);

cars3 = ["ford", "mitsubshi", "bmw", "volvo", "vw"];
cars3.sort(reverse=True, key=myFunction2);
print(cars3); #['mitsubshi', 'volvo', 'ford', 'bmw', 'vw']