# Python for loops



Com o loop `for` podemos executar um conjunto de instruções, uma vez para cada item em uma lista, tuple, set etc.

**Exemplo**

Imprima cada um dos nomes em uma lista de nomes:

```python
nomes = ["Jhon", "Mike", "Tom", "Bill"]

for i in nomes:
    print(i)

# Jhon 
# Mike 
# Tom 
# Bill    
```

Looping através de uma String:

Até mesmo as Strings são objetos iteráveis, elas contêm uma sequência de caracteres:

**Exemplo**

Loop através das letras na palavra "banana":

```python
for i in "banana":
    print(i)

# b 
# a 
# n 
# a 
# n
# a    
```

##  Declaração de Ruptura

Com a instrução `break` podemos para o loop antes que ele tenha feito o loop em todos os itens:

```python
nomes = ["Joe", "Bill", "Tom", "Mark"]

for i in nomes:
    print(i)
    if i == "Tom":
        break

# Joe 
# Bill
# Tom    
```

**Exemplo**

Saia do loop quando for "Tom", mas dessa vez  o `break` vem antes do `print`:

```python
nomes = ["Joe", "Bill", "Tom", "Mark"]

for i in nomes:
    if i == "Tom":
        break
    print(i)

# Joe 
# Bill
```

## Declaração de Continuação

Com a instrução `continue` podemos parar a iteração atual do loop, e continuar com a próxima:

Exemplo

Não imprima "Bill":

```python
nomes = ["Joe", "Bill", "Tom", "Mark"]

for i in nomes:
    if i == "Bill":
        continue
    print(i)

# Joe
# Tom
# Mark
```

## Função range()

A função `range()` retorna uma sequência de números, começando a partir de 0 por padrão, e incrementando 1 (por padrão) e termina em um número especificado:

**Exemplo**

Usando a função de intervalo:

```python
for i in range(6):
    print (i)

# 0 
# 1
# 2
# 3
# 4
# 5
```

A função `range()` tem o `0` como valor inicial padrão, no entanto, é possível especificar o valor inicial adicionando um parâmetro: `range(2, 6)`, o que significa valor entre `2` e `6`:

**Exemplo**

Usando  o parâmetro inicial:

```python
for i in range(2, 6):
    print(i)

#2
#3
#4
#5    
```

A função `range()` por padrão incrementar a sequência por 1, no entanto, é possível especificar o valor de incremento adicionando um terceiro parâmetro: `range(2, 10, 2)`

**Exemplo**

Incrementar a sequência com 2:

```python
for i in range(2, 10, 2):
    print(i)

#2
#4
#6
#8
```

## Else em For loop

O `else` em um loop especifica um bloco de código a ser executado quando o loop estiver concluído:

Exemplo

Imprima todos os números de `0` a `5` e imprima uma mensagem quando o loop terminar:

```python
for i in range(6):
    print(i)
else:
    print("Fim da contagem")    

#0
#1
#2
#3
#4
#5
#Fim da contagem    
```

> Nota: O bloco não será executado se o loop for interrompido por uma declaração `break`:

**Exemplo**

Quebre o loop quando for 3, e veja  o que acontece com o bloco `else`:

```python
for i in range(6):
    if i == 3:
        break
    print(i)
else:
    print("Fim da contagem")    

#0
#1
#2    
```

## Laços Aninhados

Um loop aninhado é um loop dentro de  outro loop.

O "loop interno" será executado uma vez para cada iteração do "loop externo":

**Exemplo**

Imprima cada adjetivo para cada fruta:

```python
adj = ["vermelho", "grande", "saborosa"]
frutas = ["maçã", "banana", "cereja"]

for i in adj:
    for j in frutas:
        print(i, j)

#vermelho maçã
#vermelho banana
#vermelho cereja
#grande maçã
#grande banana
#grande cereja
#saborosa maçã
#saborosa banana
#saborosa cereja
```

