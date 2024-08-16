# Typecasting (Convertendo de um tipo para outro)
Typecasting, type convertion ou coercion é o ato de converter um tipo em outro.

A seguir veremos algumas classes que podem fazer essas conversões, porém no momento vamos considerá-las como funções.

### int()
Converte o valor que passarmos para a função para o tipo ``int`` inteiro, contanto que o valor seja um número.

```python
print(int('1') + 1) # Saída: 2
print(int(4.8) + 5) # Saída: 9
```

### float()
Converte o valor que passarmos para a função para o tipo ``float`` flutuante, contanto que o valor seja um número.

```python
print(float('2') + 1) # Saída: 3.0
print(float('5') + 5.8) # Saída: 10.8
```

### bool()
Converte o valor que passarmos para a função para o tipo ``bool`` booleano, contanto que o valor seja uma expressão ou possa ser transformado em booleano.

```python
# '' = falso
print(bool('')) # Saída: False

# ' ' = verdadeiro
print(bool(' ')) # Saída: True

# Uma expressão que verifica se a soma é igual a 8
print(bool(2 + 5 == 8)) # Saída: False
```

### str()
Converte o valor que passarmos para a função para o tipo ``str`` string.

```python
print(str(11) + 'b') # Saída: 11b
print(str(True) + ' -> Vini') # Saída: True -> Vini
```
