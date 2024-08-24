# Introdução a operadores

## Operadores aritméticos

Os operadores aritméticos nós já conhecemos quando estudamos matemática. 

São os operadores matemáticos que utilizamos para realizar cálculos, desde a soma até a exponenciação.

### +
Utilizado para fazer somas ou adições.

```python
soma = 12 + 8
print('Soma ->', soma)

# Saída: Soma -> 20
```

Utilizado também para fazer concatenações.

> [!NOTE]
> Concatenação é o ato de juntar, unir. <br>
> Só é possível fazer entre **strings**.


```python
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

# Saída: A B C
```

### -
Utilizado para calcular a diferença entre dois números, ou seja, fazer subtrações.

```python
subtracao = 10 - 6
print('Subtração ->', subtracao)

# Saída: Subtração -> 4
```

### *
Utilizado para calcular o produto da multiplicação entre dois números.

```python
multiplicacao = 5 * 4
print('Multiplicação ->', multiplicacao)

# Saída: Multiplicação -> 20
```

Utilizado também para fazer repetições. 

> [!IMPORTANT]
> É necessário ter um número e uma string, independente da ordem.

```python
a_dez_vezes = 'A' * 10
print(a_dez_vezes)

# Saída: AAAAAAAAAA

luiz_tres_vezes = 2 * 'Luis'
print(luiz_tres_vezes)

# Saída: LuisLuisLuis
```




### /
Utilizado para calcular o quociente da divisão entre dois números. O resultado será do **tipo flutuante (float)**.

```python
divisao = 5 / 1.6
print('Divisão ->', divisao)

# Saída: Divisão -> 3.125
```

### //
Utilizado para calcular o quociente da divisão entre dois números. O resultado será do **tipo inteiro (int)**.

>[!IMPORTANT]
> Há casos em que o resultado será com ponto flutuante, porém, diferentemente da divisão anterior, o resultado terá APENAS uma casa decimal.

```python
divisao_inteira = 10 // 2.2
print('Divisão Inteira ->', divisao_inteira)

# Saída: Divisão Inteira -> 4.0
```

### **
Utilizado para calcular uma potência.

```python
exponenciacao = 2 ** 10
print('Exponenciação ->', exponenciacao)

# Saída: Exponenciação -> 1024
```

### %
Utilizado para calcular o resto da divisão.

> [!NOTE]
> Exemplo de onde utilizamos: 
> 
> Verificando se um número é par ou ímpar; <br> Verificando um número é múltiplo de outro.

```python
modulo = 25 % 5
print('Módulo ->', modulo)

# Saída: Módulo -> 0
```
<br>

## Precedência entre os operadores
A precedência nada mais é do que a ordem em que as operações serão feitas em uma expressão numérica.

### 1º. ( ) 
Tudo o que estiver dentro dos parênteses será resolvido primeiro.

Caso haja mais de um par de parênteses, a prioridade será resolver os mais internos até o mais externo.

```python
print(2 + 2)
# Saída: 4

print(2 + (5 - 4))
# Saída: 3

print(4 * (10 - (5 + 3)))
# Saída: 32
```

### 2º. **
As potências (um número elevado a um expoente).

### 3°. * / // %
As operações de multiplicação, divisão, divisão inteira e módulo.

### 4°. + -
As operações de soma ou adição e subtração.




