# Introdução

O [Python](https://www.python.org) é uma linguagem de programação com **tipagem dinâmica e forte**, portanto não é necessário identificar se uma variável é do tipo string ou inteiro, por exemplo, já que o interpretador do python identifica automaticamente.

<br>

> [!NOTE]
> **Tipagem dinâmica:**<br>
> É a capacidade que uma linguagem de programação tem de detectar automaticamente o tipo de qualquer dado que seja informado.

<br>

> [!NOTE]
> **Tipagem forte:**<br>
> A linguagem de programação impõe regras mais rigorosas em relação à manipulação de tipos de dados. Nesse tipo de linguagem, não é possível somar um texto a um número, por exemplo.  

<br>

Ex.1: O tipo da variável é detectado através do valor atribuido a ela.

```python
idade = 25
# A variável é do tipo inteiro

nome = "Alice"
# A variável é do tipo string
```

Ex.2: O tipo de argumento passado para uma função é detectado automaticamente.

```python
print("Pedro")
# Detecta que o argumento é do tipo string

print(123)
# Detecta que o argumento é do tipo inteiro
```
<br>

# Tipos de Dados

### String
É o tipo de dado usado para textos, podendo ser o nome de uma pessoa até um parágrafo, por exemplo. 

No python, as strings sempre estão dentro de aspas simples ou duplas e é escrito como *``str``*.

```python
# String com aspas simples
print('Ana Júlia')

# String com aspas duplas 
print("Hester Maria")
```

É possível fazer com que apareça aspas dentro de um texto, basta fazer o seguinte:

1- Caso você queira que seja exibido as aspas duplas, basta fazer a string com as aspas simples e no texto colocar as aspas duplas.
```python
print('Ana Júlia "Aprovada"')
# Saída: Ana Júlia "Aprovada"
```

1- Caso você queira que seja exibido as aspas simples, basta fazer a string com as aspas duplas e no texto colocar as aspas simples.
```python
print("João Pedro 'Reprovado'")
# Saída: João Pedro 'Reprovado'
```

### Integer
É o tipo de dado usado para números inteiros, podendo ser positivo ou negativo.

No Python é escrito como *``int``*.

```python
print(11) # Saída: 11
print(-11) # Saída: -11
print(0) # Saída: 0
```

### Float
É o tipo de dado usado para o que chamamos de números de ponto flutuante, ou seja, números com casas decimais.

No Python é escrito da mesma forma, sendo *``float``*.

>[!IMPORTANT]
> Na programação você SEMPRE deverá usar o ponto para separar as casas decimais de um número.

```python
print(1.1, 10.11) # Saída: 1.1 10.11
print(0.0, -1.5)  # Saída: 0.0, -1.5
```

### Boolean
É o tipo de dado usado para analisar os valores de uma expressão ou comparação e retornar um valor booleano, isto é,  ``True`` (verdadeiro) ou ``False`` (falso).

No Python é escrito como *``bool``*.

Podemos construir comparações através de operadores relacionais, são eles:


| Caractere | Conceito         | Exemplo    |
| ---       | ---              | ---        |
| !=        | Diferente de     | 2 != 3     |
| >         | Maior que        | 5 > 4      |
| <         | Menor que        | 1 < 8      |
| >=        | Maior ou igual   | nota >= 6  |
| <=        | Menor ou igual   | nota <= 5  |

<br>

```python
print(8 == 8) # Saída: True
print(10 == 5.1) # Saída: False

altura = 1.72
print(altura >= 1.60) # Saída: True

print("Ana" != "Ana") # Saída: False
```
<br>

# Função type()
É uma função que retorna o tipo de dado de uma determinada variável, valor ou argumento.

```python
print(type(2)) # Saída: <class 'int'>
print(type('Ruth')) # Saída: <class 'str'>
print(type(False)) # Saída: <class 'bool'>

# Retorna o tipo bool porque é uma comparação
print(type(2 == 2)) # Saída: <class 'bool'>

print(type(1.2)) # Saída: <class 'float'>
```
