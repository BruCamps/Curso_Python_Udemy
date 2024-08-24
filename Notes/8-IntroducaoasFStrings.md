# Introdução às F-Strings (formatação de strings)

Para evitar precisar colocar um texto grande dentro de uma função como no print() e/ou colocar sinais para concatenar as funções, palavras ou variáveis, é possível armazenar tudo isso numa variável de um jeito simples. Confira abaixo:

1° passo: Envolver tudo entre aspas

```python
linha_1 = 'O(a) estudante nome_estudante tem idade anos e estuda no turno da turno'
```

2° passo: Adicionar a letra **f** minúscula antes do primeiro sinal de aspas

> [!NOTE]
> Esse f significa formatação

```python

linha_1 = f'O(a) estudante nome_estudante tem idade anos e estuda no turno da turno'
```

3° passo: Colocar as variáveis em evidencia, envolvendo-as entre chaves

```python
linha_1 = f'O(a) estudante {nome_estudante} tem {idade} anos e estuda no turno da {turno}'
```

4° passo: Adicionar a variável na função print para exibir o texto completo

```python
nome_estudante = 'Maya'
idade = 10
turno = 'manhã'
linha_1 = f'O(a) estudante {nome_estudante} tem {idade} anos e estuda no turno da {turno}'

print(linha_1)
# Saída: O(a) estudante Maya tem 10 anos e estuda no turno da manhã
```

Também é possível formatar as casas decimais de um número, observe abaixo:

1° passo: Colocar a variável entre chaves

```python
linha_1 = f'O peso de Ana é {peso}'
```

2° passo: Colocar após a variável **:.**, depois o **número de casas decimais** e a letra **f**.

Ficando como nos exemplos: ``:.2f``, ``:.4f``

```python
linha_1 = f'O peso de Ana é {peso:.2f}'
```

3° passo: Adicionar a variável na função print para exibir o texto completo

```python
peso = 29.98769
linha_1 = f'O peso de Ana é {peso:.2f}'

print(linha_1)
# Saída: O peso de Ana é 29.99
```

