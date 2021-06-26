frutas = ["banana", "melão", "uva"];
frutas.append("limão");

print(frutas); #['banana', 'melão', 'uva', 'limão']

#adiciona uma lista dentro de outra lista
cars = ["bmw", "volvo", "porsche"];
cars.append(frutas);
print(cars); #['bmw', 'volvo', 'porsche', ['banana', 'melão', 'uva', 'limão']]