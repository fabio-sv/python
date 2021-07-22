# Python - Dicionários

## dicionário

Dicionários são usados para armazenar valores de dados em pares de valores chave.

Um dicionário é uma coleção que é encomendada, mutável e não permite duplicatas.

Os dicionários são escritos com suportes cacheados e têm chaves e valores:

```python
my_dict = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2021
}

print(my_dict)

#{'marca': 'Ford', 'modelo': 'Mustang', 'ano': 2021}
```

## Itens do dicionário

Os itens do dicionário são pedidos, mutáveis e não permitem duplicatas.

Os itens do dicionário são apresentados em pares de valores chave e podem ser referidos usando o nome da chave.

### Exemplo

Imprima o valor "marca" do dicionário:

```python
my_dict = {
    "marca": "Porsche",
    "modelo": "911 Turbo S",
    "ano": "2021"
}

print(my_dict["marca"])

#Porsche
```

## Ordenado ou desordenado?

Quando dizemos que os dicionários são ordenados, significa que os itens têm uma ordem definida, e essa ordem não mudará.

Desordenado significa que os itens não têm uma ordem definida, você não pode se referir a um item usando um índice.

## Mutável

Os dicionários são mutáveis, o que significa que podemos alterar, adicionar ou remover itens após a criação do dicionário.

## Duplicatas não permitidas

Os dicionários não podem ter dois itens com a mesma chave:

```python
my_dict = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "2020",
    "ano": "2021"
}

print(my_dict)

#{'marca': 'Ford', 'modelo': 'Mustang', 'ano': '2021'}
```

## Comprimento do dicionário

Para determinar quantos itens um dicionário tem, use a função ` len()`:

### Exemplo

Imprima o número de itens no dicionário:

```python
my_dict = {
    "marca": "VW",
    "modelo": "Golf",
    "ano": "2021"
}

print(len(my_dict))

#3
```

## Itens do Dicionário - Tipos de Dados

Os valores em itens de dicionário podem ser de qualquer tipo de dados:

### Exemplo

Tipos de dados de `string`, ` int`, `boolean` e `list`:

```python
carro = {
    "marca": "Porsche",
    "eletrico": False,
    "ano": 2020,
    "cores": ["branco", "preto", "cinza"]
}

print(carro)

#{'marca': 'Porsche', 'eletrico': False, 'ano': 2020, 'cores': ['branco', 'preto', 'cinza']}
```

## Tipo

Do ponto de vista do Python, os dicionários são definidos como objetos com o tipo de dados  `dict`:

`<class 'dict'>`

### Exemplo

Imprima o tipo de dados de um dicionário:

```python
my_dict = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2020
}

print(type(my_dict))

#<class 'dict'>
```

## Coleções Python (Arrays)

Existem quatro tipos de dados de coleta na linguagem de programação Python:

- **List** é uma coleção que é encomendada e mutável. Permite membros duplicados.
- **Tuple** é uma coleção que é ordenada e imutável. Permite membros duplicados.
- **Set** é uma coleção que não é ordenada e é desindexada. Sem membros duplicados.
- **Dictionary** é uma coleção que é ordenada e mutável. Sem membros duplicados.

Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo. Escolher o tipo certo para um determinado conjunto de dados pode significar retenção de significado, e isso pode significar um aumento na eficiência ou segurança.

# Python - Itens do Dicionário de Acesso

## Acessando itens

Você pode acessar os itens de um dicionário referindo-se ao seu nome-chave, dentro de suportes quadrados:

### exemplo

Obtenha o valor da chave "modelo":

```python
my_dict = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2020
}

x = my_dict["modelo"]

print(x)

#Mustang
```

Há também um método chamado que lhe dará o mesmo resultado:`get()`

### Exemplo

Obtenha o valor da tecla "modelo":

```python
my_dict = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2020
}

x = my_dict.get("modelo")

print(x)

#Mustang
```

## Obter chaves

O método `keys()` retornará uma lista de todas as chaves do dicionário.

### Exemplo

Obtenha uma lista das chaves:

```python
my_dict = {
    "marca": "Porsche",
    "modelo": "Carrera GT",
    "ano": 2020
}

x = my_dict.keys()

print(x)

#dict_keys(['marca', 'modelo', 'ano'])
```

A lista das chaves é uma *exibição* do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de chaves.

### Exemplo

Adicione um novo item ao dicionário original e veja se a lista de chaves também é atualizada:

```python
carro = {
    "marca": "Ferrari",
    "modelo": "Monza",
    "ano": 2020
}

x = carro.keys()

print(x)

#dict_keys(['marca', 'modelo', 'ano'])

carro["cor"] = "Vermelho"

print(x)

#dict_keys(['marca', 'modelo', 'ano', 'cor'])
```

## Valores de alteração

Você pode alterar o valor de um item específico referindo-se ao seu nome-chave:

### Exemplo

Mude o "ano" para 2018:

```python
my_dict = {
    "marca": "General Motors",
    "modelo": "Camaro",
    "ano": 2020
}

my_dict["ano"] = 2021

print(my_dict)

#{'marca': 'General Motors', 'modelo': 'Camaro', 'ano': 2021}
```

O método `update()` atualizará o dicionário com os itens do argumento dado.

O argumento deve ser um dicionário ou um objeto iterável com pares de valores chave.

### exemplo

Atualize o "ano" do carro usando o método `update()`:

```

```

[Python - Alterar itens do dicionário (w3schools.com)](https://www.w3schools.com/python/python_dictionaries_change.asp)