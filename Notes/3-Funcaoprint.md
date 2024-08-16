# Função print()

O ``print()`` é uma função do python que manda algo para a saída do terminal (output) quando executada.

O print em português é "imprimir", no mundo real relacionamos a palavra ao papel, mas na computação em geral é mostrar algo na tela. 

>[!IMPORTANT]
> Em termos simples, a função ``print()`` é usada para exibir coisas na tela.


>[!NOTE]
> Toda função precisa dos parênteses para receber argumentos.

Como argumentos podemos ter textos, números e até mesmo outras funções
```python
print(12)
# Saída: 12
print("Chocolate")
# Saída: Chocolate
```

Para exibir mais de um argumento em um único print, utilize a vírgula para separar os argumentos
```python
print(12, 34)
# Saída: 12 34
print(56, 78)
# Saída: 56 78
```
Haver espaço entre os argumentos é algo padrão do Python. Podemos personalizar isso se desejarmos, a partir do argumento ``sep=""`` ou ``sep=''``
```python
print(12, 34, sep="") # Não há separador
# Saída: 1234

print(12, 34, sep=" ") # O separador será o espaço
# Saída: 12 34

print(12, 34, sep='-') # O separador será o hífen
# Saída: 12-34

print(12, 34, sep='J') # O separador será o J
# Saída: 12J34

print(12, 34, sep='90') # O separador será o 90
# Saída: 129034
```

O que você desejar colocar como separador, seja um caractere especial, número ou letra será definido como o separador.

<br>

Ao observar os resultados de prints seguidos no terminal, há sempre uma quebra de linha, outro padrão evidente na linguagem. Essa quebra de linha é feita a partir de um ou dois caracteres dependendo do sistema operacional usado, vamos conferir:
```python
# Caracteres de quebra de linha

# CRLF -> Carriage Return (\r) Line Feed (\n)
# \r\n (Sistema: Windows mais antigo)

# LF -> Line Feed (\n)
# \n (Sistemas: Mac, Linux, Unix e Windows mais recente)
```
Também podemos personalizar isso se desejarmos, a partir do argumento ``end=""`` ou ``end=''``
```python
print(14, 8, 24, sep="/", end="") # Nada acontece
print(200, 400, 600, sep='-', end='\n') # Quebra de linha
print(6000, 800, sep=' ', end="") # Nada acontece

# Saída:  
# 14/8/24200-400-600
# 6000 800
```

Podemos misturar textos, caracteres especiais e números com essas quebras de linha

```python
print(14, 8, 24, sep="/", end="#031\n") # No fim da linha terá uma hastag e a quebra de linha
print(200, 400, 600, sep='-', end='\nFim do Código') # Quebra de linha e a próxima linha começará com o texto

# Saída: 
# 14/8/24#031
# 200-400-600
# Fim do Código
```
