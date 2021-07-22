# Matrizes Python

> **Nota:** Python não tem suporte integrado para Arrays, mas [python Lists](https://www.w3schools.com/python/python_lists.asp) pode ser usado em vez disso

## Matrizes

> **Nota:** Este tutorial mostra como usar LISTS como ARRAYS, no entanto, para trabalhar com arrays em Python você terá que importar uma biblioteca, como a [biblioteca NumPy](https://www.w3schools.com/python/numpy/default.asp).

Os arrays são usados para armazenar vários valores em uma única variável:

**Exemplo**

Crie uma matriz contendo nomes de carros:

```python
carros = ["Volvo", "Porsche", "Ford"]
```

## Acesse os elementos de uma matriz

Você se refere a um elemento de matriz referindo-se ao número do *índice*.

**Exemplo**

Obtenha o valor do primeiro item de matriz:

```python
carros = ["Volvo", "Porsche", "Ford"]

print(carros[0])

#Volvo
```

**Exemplo**

Modifique o valor do primeiro item de matriz:

```python
carros = ["Volvo", "Porsche", "Ford"]

carros[0] = "BMW"

print(carros[0])

#BMW
```

## O Comprimento de uma Matriz

Use o método `len()` para retornar o comprimento de uma matriz (o número de elementos em uma matriz).

**Exemplo**

Retorne o número de elementos na matriz carros:

```python
carros = ["Volvo", "Porsche", "Ford"]

x = len(carros)
print(x)

#3
```

## Elementos da matriz em looping

Você pode usar o `for in` loop para percorrer através de todos os elementos de uma matriz.

**Exemplo**

Imprima cada item na matriz carros:

```python
carros = ["Volvo", "Porsche", "Ford"]

for i in carros:
    print(i, end=", ")

#Volvo, Porsche, Ford,     
```

## Adicionando elementos de matriz

Você pode usar o método `append()` para adicionar um elemento de uma matriz.

**Exemplo**

Adicione mais um elemento à matriz carros:

```python
carros = ["Volvo", "Porsche", "Ford"]

carros.append("BMW")
print(carros)

#['Volvo', 'Porsche', 'Ford', 'BMW']
```

## Removendo elementos de matriz

Você pode usar o método para remover um elemento da matriz.`pop()`

**Exemplo**

Exclua o segundo elemento da matriz carros:

```python
carros = ["Volvo", "Porsche", "Ford"]

carros.pop(1)
print(carros)

#['Volvo', 'Ford']
```

Você também pode usar o método para remover um elemento da matriz.`remove()`

**Exemplo**

Exclua o elemento que tem o valor "Volvo":

```python
carros = ["Volvo", "Porsche", "Ford"]

carros.remove("Volvo")
print(carros)

#['Porsche', 'Ford']
```

> **Nota:** O método `remove()` da lista remove apenas a primeira ocorrência do valor especificado.

## Métodos de matriz

Python tem um conjunto de métodos incorporados que você pode usar em listas/matrizes.

| Método     | Descrição |
| ---------- | --------- |
| `append()` |           |
| `clear()`  |           |
| `copy()`   |           |
| `count()`  |           |
| `extend()` |           |
| `index()`  |           |
| `insert()` |           |

