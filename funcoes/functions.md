# Funções Python

Uma função é um bloco de código que só funciona quando é chamado.

Você pode passar dados, conhecidos como parâmetros, para uma função.

Uma função pode retornar dados como resultado.

## Criando uma função

Em Python, uma função é definida usando a palavra-chave `def`:

**Exemplo**

```python
def my_function():
    print("Minha função Python!")

my_function()    

#Minha função Python!
```

## Argumentos

Informações podem ser passadas em funções como argumentos.

Os argumentos são especificados após o nome da função, dentro dos parênteses. Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

O exemplo a seguir tem uma função com um argumento (fnome). Quando a função é chamada, passamos um primeiro nome, que é usado dentro da função para imprimir o nome completo:

**Exemplo**

```python
def my_function(fname):
    print(fname + " Santos", end=", ")

my_function("Tom")
my_function("Bill")
my_function("Oliver")

#Tom Santos, Bill Santos, Oliver Santos,
```

## Número de argumentos

Por padrão, uma função deve ser chamada com o número correto de argumentos. O que significa que se sua função espera 2 argumentos, você tem que chamar a função com 2 argumentos, não mais, e não menos.

### Exemplo

Esta função espera 2 argumentos, e obtém 2 argumentos:

```python
def function(fname, lname):
    print(fname + " " + lname)

function("Tom", "Santos")

#Tom Santos
```

> Se você tentar chamar a função com 1 ou 3 argumentos, você terá um erro.

## Argumentos Arbitrários, *args

Se você não sabe quantos argumentos serão passados para sua função, adicione um `*` antes do nome do parâmetro na definição da função.

Desta forma, a função receberá uma *tupla* de argumentos, e você pode acessar os itens de acordo:

### Exemplo

Se o número de argumentos for desconhecido, adicione um `*` antes do nome do parâmetro:

```python
def function(*cars):
    print("My Cars: " + cars[2])

function("BMW", "Volvo", "Ford")

#Carros: Ford
```

## Argumentos de palavras-chave

Você também pode enviar argumentos com a *chave* = valor.

Dessa forma, a ordem dos argumentos não importa.

### Exemplo

```python
def function(car3, car2, car1):
    print("My car: " + car3)

function(car1="Volvo", car2="Porsche", car3="Evoque")    

#My car: Evoque
```

## Argumentos arbitrários de palavras-chave, **kwargs

Se você não sabe quantos argumentos de palavra-chave serão passados para sua função, adicione dois asterisco `**` antes do nome do parâmetro na definição da função.

Desta forma, a função receberá um *dicionário* de argumentos, e poderá acessar os itens de acordo:

### Exemplo

Se o número de argumentos de palavras-chave for desconhecido, adicione um `**` duplo antes do nome do parâmetro:

```python
def function(**name):
    print("Meu sobrenome é " + name["lname"])

function(fname = "Tom", lname = "Santos")

#Meu sobrenome é Santos
```

## Valor de parâmetro padrão

O exemplo a seguir mostra como usar um valor de parâmetro padrão.

Se chamarmos a função sem argumento, ela usará o valor padrão:

**Exemplo**

```python
def function(pais = "Brasil"):
    print("Meu pais: " + pais)

function("Alemanha")   
function("Noruega")
function()
function("Bélgica") 

#Meu pais: Alemanha
#Meu pais: Noruega        
#Meu pais: Brasil
#Meu pais: Bélgica 
```

## Passando uma lista como argumento

Você pode enviar qualquer tipo de argumento de dados para uma função (string, number, list, dictionary etc.), e ele será tratado como o mesmo tipo de dados dentro da função.

Por exemplo, se você enviar uma lista como argumento, ela ainda será uma lista quando chegar à função:

### Exemplo

```python
def function(frutas):
    for i in frutas:
        print(i, end=", ")

minhas_frutas = ["banana", "laranja", "uva"] 

function(minhas_frutas)

#banana, laranja, uva,
```

## Valores de retorno

Para deixar uma função retornar um valor, use a instrução `return`:

### Exemplo

```python
def multiplicacao(valor):
    return 5 * valor

print(multiplicacao(2))
print(multiplicacao(3))
print(multiplicacao(4))
print(multiplicacao(5))

#10
#15
#20
#25
```

## Declaração de passe

As funções não podem ser vazias, mas se você por algum motivo tiver uma função sem conteúdo, coloque `pass` na instrução para evitar um erro.

```python
def function():
	pass 
```

