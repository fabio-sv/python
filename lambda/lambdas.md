# Python Lambda

Uma função lambda é uma pequena função anônima.

Uma função lambda pode ter qualquer número de argumentos, mas só pode ter uma expressão.

## sintaxe

```
lambda argumento : expressão
```

A expressão é executada e o resultado é devolvido:

**Exemplo**

Adicione 10 ao argumento `a` e devolva o resultado:

```python
x = lambda a : a + 10
print(x(5))

#15
```

As funções lambda podem ter qualquer número de argumentos:

**Exemplo**

Multiplique o argumento `a` com argumento `b` e retorne o resultado:

```python
x = lambda a, b : a * b
print(x(5, 6))

#30
```

**Exemplo**

Resumir o argumento `a`, `b`, `c` , e retornar o resultado:

```python
x = lambda a, b, c : a + b + c
print(x(10, 20, 30))

#60
```

## Por que usar funções lambda?

O poder da lambda é melhor mostrado quando você os usa como uma função anônima dentro de outra função.

Digamos que você tenha uma definição de função que leva um argumento, e esse argumento será multiplicado com um número desconhecido:

```python
def myfunction(n):
return lambda a : a * n
```

Use essa definição de função para fazer uma função que sempre dobre o número que você envia:

**Exemplo**

```python
def my_function(n):
    return lambda a : a * n

dobro = my_function(2)
print(dobro(11))

#11
```

Ou, use a mesma definição de função para fazer uma função que sempre *triplique* o número que você envia:

**Exemplo**

```python
def my_function(n):
    return lambda a : a * n

dobro = my_function(2)
triplo = my_function(3)

print(dobro(11))
print(triplo(11))

#22
#33
```

