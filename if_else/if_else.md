## Condições de Python e suas  declarações

Python suporta as condições lógicas usuais da matemática:

- Iguais: `a == b`
- Não é igual: `a != b`
- Menor: `a < b`
- Menor ou igual:  `a <= b`
- Maior que: `a > b`
- Maior ou igual: `a >= b`

Essas condições podem ser usadas de várias maneiras, mais comumente em "if declarações" e loops.

Uma "declaração if" é escrita usando a palavra-chave if.

### Exemplo

If declaração:

```python
a = 33
b = 200

if b > a:
    print("b é maior que a...")

#b é maior que a...    
```

## Elif

A palavra-chave elif é uma maneira de dizer "se as condições anteriores não eram verdadeiras, então tente esta condição".

### Exemplo

```python
a = 33
b = 33

if b > a:
    print("b é maior que a")
elif a == b:
    print("a é igual a b")    

#a é igual a b    
```

## Else

A `else` palavra-chave pega qualquer coisa que não seja capturada pelas condições anteriores.

### Exemplo

```python
a = 200
b = 33

if b > a:
    print("b é maior do que a")
elif a == b:
    print("a é igual a b")
else:
    print("a é maior que b")        

#a é maior que b    
```

## Mão curta IF

Se você tiver apenas uma instrução para executar, você pode colocá-la na mesma linha que a instrução if.

### Exemplo

Declaração `if ` de uma linha:

```python
a = 10
b = 5

if a > b: print("a é maior que b")

#a é maior que b
```

Se você tiver apenas uma instrução para executar, uma para `if` e outra para `else`, você pode colocar tudo na mesma linha:

### Exemplo

Declaração `if ` `else` de uma linha:

```python
a = 2
b = 300

print("A") if a > b else print("B")

#B
```

> Esta técnica é conhecida como **Operadores Ternários**, ou **Expressões Condicionais**.

Você também pode ter várias outras afirmações na mesma linha:

```python
a = 300
b = 300

print("A") if a > b else print("igual") if a == b else print("B")

#igual
```

## And

A palavra-chave `and` é um operador lógico, e é usada para combinar declarações condicionais:

### Exemplo

Teste se `a` é maior que `b` e se `c` é maior que `a` :

```python
a = 200
b = 33
c = 500

if a > b and c > a:
    print("A condição é verdadeira")

#A condição é verdadeira    
```

## Or

A palavra-chave `or` é um operador lógico, e é usada para combinar declarações condicionais:

### Exemplo

Teste se `a` é maior que `b` ou se `a` é maior que `c` :

```python
a = 200
b = 33
c = 500

if a > b or a > c:
    print("A condição é verdadeira")

#A condição é verdadeira    
```

## A declaração de passe

`if ` declarações não podem estar vazias, mas se você por algum motivo tiver uma declaração sem conteúdo, coloque `pass` na declaração para evitar um erro.

```python
a = 10
b = 20

if b > a:
    pass
```

