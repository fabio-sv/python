# Laços Python

Python tem dois comandos de loop primitivos.

- `while` loop

- `for` loop

## O loop while

Com o `while` podemos executar um conjunto de declarações, desde que uma condição seja verdadeira.

**Exemplo**

Imprima `i ` desde que seja menor que `6`.

```python
i = 1

while i < 6:
    print(i)
    i += 1
```

> Nota: lembre-se de incrementar i, ou então o loop continuará para sempre.

## Declaração de Ruptura

Com uma instrução `break `, podemos parar o loop mesmo que a condição ainda seja verdadeira.

**Exemplo**

Saia do loop quando estiver em 3:

```python
i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

    #0 1 2 3
```

## Declaração de Continuação

Com a declaração `continue` podemos parar a iteração atual, e continuar com a próxima:

**Exemplo**

Continue para a próxima iteração se eu tiver 3:

```python
i = 0 
while i < 6:
    i += 1

    if i == 3:
        continue
    print(i)

    #1 2 4 5 6
```

##  Else declaração

Com a `else` instrução, podemos executar um bloco de código uma vez quando a condição não é mais verdadeira:

**Exemplo**

Imprima uma mensagem quando a condição for falsa:

```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i não é mais menor do que 6")    

# 1
# 2 
# 3 
# 4 
# 5 
# 6 
# i não é mais menos do que 6
```

