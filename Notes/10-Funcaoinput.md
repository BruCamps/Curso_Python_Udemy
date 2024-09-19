# Função input()
Utilizada para coletar dados do usuário. É o espaço em que o usuário poderá digitar.

```python
input("Digite algo -> ")
# Saída: Digite algo ->
```

Podemos passar essa função para uma variável

```python
nome = input("\nQual é o seu nome? ")
print(f'O seu nome é {nome}\n')
```

![alt text](https://github.com/BruCamps/Curso_Python_Udemy/blob/main/Images/image.png)


```python
nome = input("\nQual é o seu nome? ")
print(f'O seu nome é {nome=}\n')
```

![alt text](https://github.com/BruCamps/Curso_Python_Udemy/blob/main/Images/image-1.png)

### Como receber números em um input
Toda resposta em um input é string por padrão, e para que seja reconhecida como um número, devemos fazer a conversão de tipo.

### Forma nº 1 (conversão direta)

```python
numero_1 = int(input("\nDigite um número: ")) # Converte para inteiro SOMENTE quando a resposta NÃO É TEXTO
numero_2 = int(input("\nDigite outro número: ")) # Converte para inteiro SOMENTE quando a resposta NÃO É TEXTO

print(f'\nA soma dos números é {int_numero_1 + int_numero_2}\n')
```

> [!TIP]
> Se for necessário verificar o que foi digitado pelo usuário, a 1ª forma não é recomendada.

### Forma nº 2 (conversão indireta)

```python
numero_1 = input("\nDigite um número: ")
numero_2 = input("\nDigite outro número: ")

int_numero_1 = int(numero_1) # Transforma a resposta em inteiro
int_numero_2 = int(numero_2) # Transforma a resposta em inteiro

print(f'\nA soma dos números é {int_numero_1 + int_numero_2}\n')
```
