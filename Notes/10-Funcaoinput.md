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

![alt text](image.png)


```python
nome = input("\nQual é o seu nome? ")
print(f'O seu nome é {nome=}\n')
```

![alt text](image-1.png)

Para receber números em um input, siga o exemplo abaixo:

```python
numero_1 = input("\nDigite um número: ")
numero_2 = input("\nDigite outro número: ")

int_numero_1 = int(numero_1) # Transformar a resposta em inteiro
int_numero_2 = int(numero_2) # Transformar a resposta em inteiro

print(f'\nA soma dos números é {int_numero_1 + int_numero_2}\n')
```
