# Python - Join Sets

## Junte os dois conjuntos

Existem várias maneiras de se juntar dois ou mais conjuntos em Python.

Você pode usar o método que retorna um novo conjunto contendo todos os itens de ambos os conjuntos ou o método que insere todos os itens de um conjunto em outro:`union()``update()`

### Exemplo

O método retorna um novo conjunto com todos os itens de ambos os conjuntos:`union()`

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)

#{1, 2, 3, 'b', 'c', 'a'}
```

### Exemplo

O método `update()` insere os itens do conjunto2 no conjunto1:

```python
#O método insere os itens no conjunto2 no conjunto1:update()

my_set1 = {"a", "b", "c"}
my_set2 = {1, 2, 3}

my_set1.update(my_set2)

print(my_set1)

#{1, 2, 3, 'a', 'b', 'c'}
```

> **Nota:** Ambos e excluirão quaisquer itens duplicados.`union()``update()`

## Mantenha apenas as duplicatas

O método `intersection_update()` manterá apenas os itens presentes em ambos os conjuntos.

### Exemplo

Retorna o item que se repete de  `x` em `y`:

```python
x = {"apple", "banana", "chery"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#{'apple'}
```

O método `intersection()` retornará um *novo* conjunto, que contém apenas os itens presentes em ambos os conjuntos.

### Exemplo

Devolva um conjunto que contenha os itens existentes em ambos os conjuntos `x` e conjuntos`y`:

```python
x = {"apple", "banana", "chery"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#{'apple'}
```

[Python - Join Sets (w3schools.com)](