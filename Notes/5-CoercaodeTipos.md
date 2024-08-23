# Typecasting (Convertendo de um tipo para outro)
Typecasting, type convertion ou coercion é o ato de converter um tipo em outro.

A seguir veremos algumas classes que podem fazer essas conversões, porém no momento vamos considerá-las como funções.

### int()
Converte o valor que passarmos para a função para o tipo ``int``, que se refere ao tipo inteiro, contanto que o valor seja um número.

```python
print(int('1') + 1) # Saída: 2
print(int(4.8) + 5) # Saída: 9
```

### float()
Converte o valor que passarmos para a função para o tipo ``float``, que se refere ao tipo flutuante, contanto que o valor seja um número.

```python
print(float('2') + 1) # Saída: 3.0
print(float('5') + 5.8) # Saída: 10.8
```

### bool()
Converte o valor que passarmos para a função para o tipo ``bool``, que se refere ao tipo booleano, contanto que o valor seja uma expressão ou possa ser transformado em booleano.

```python
# '' = falso
print(bool('')) # Saída: False

# ' ' = verdadeiro
print(bool(' ')) # Saída: True

# Uma expressão que verifica se a soma é igual a 8
print(bool(2 + 5 == 8)) # Saída: False
```

### str()
Converte o valor que passarmos para a função para o tipo ``str``, que se refere ao tipo string.

```python
print(str(11) + 'b') # Saída: 11b
print(str(True) + ' -> Alex') # Saída: True -> Alex
```
<br>

---


### type()

Para identificar o tipo de dado de uma variável, expressão ou valor, utilizamos a função ``type()``

```python
print(1, type('1')) # Saída: 1 <class 'str'>
print(type(float('1')), type(int('1'))) # Saída: <class 'float'> <class 'int'>
```
