# Identação é a tabulação (quando damos TAB no código) e é OBRIGATÓRIO no Python


# # É possível colocar o resultado do if na mesma linha que a condição SE for APENAS 1 instrução
# numero = 15
# if numero == 15: print("Verdadeiro")
# else: print("Falso")
# # Saída: Falso

# # Continuação da linha com \ (Exemplo 1)
# total = 4 + \
#         7 + \
#         5
# print(total)
# # Saída: 16

# # Continuação da linha com \ (Exemplo 2)
# nome = 'Maria', \
#        'Luiza', \
#        'Paulo'
# print(nome)


# # Trabalhando Strings

# # Strings com várias linhas (DocString), será exibida da forma que for escrita no código com todos os espaços e TABs
# texto = '''
#     Este texto é de várias linhas
#         Este texto é de várias linhas
#             Este texto é de várias linhas
#                     Este texto é de várias linhas
#     '''
# print(texto)

# # Manipulação de Strings

# # len() -> Retorna a quantidade de caracteres de uma String (TUDO é considerado)

# # Exemplo 1
# nome = 'Ana Júlia'
# print(len(nome))
# # Saída: 9

# # Exemplo 2
# nome2 = 'João Felipe'
# print(len(nome2))
# # Saída: 11


# # Concatenação de Strings com +
# nome = input('Informe seu nome: ')
# sobrenome = input('Informe seu sobrenome: ')
# resultado = nome + ' ' + sobrenome     # O ' ' adiciona um espaço entre as strings
# print(resultado)


# # Verificar se um valor ou caractere está presente numa String com in
# email = input("Digite seu e-mail: ")
# if '@' in email: # Verifica se há o caractere @ no e-mail digitado
#     print("E-mail válido")
# else:
#     print("E-mail inválido! Não possui @.")


# in -> Verifica se tem um valor ou caractere numa string
# not in -> Verifica se NÃO tem um valor ou caractere numa string

# # Método upper() -> Retorna a string em letras maiúsculas

# Exemplo 1
# texto = 'Texto exemplo'
# print(texto.upper())
# # Saída: TEXTO EXEMPLO

# # Exemplo 2
# nome = input("Digite um nome a ser pesquisado: ")
# nomeGuardado = "Bruna"
# if nome.upper()==nomeGuardado.upper(): # Verifica se o nome guardado é igual ao nome digitado e transforma tudo em MAIÚSCULO
#     print("O nome digitado é o mesmo que está armazenado")
# else:
#     print("Os nomes são diferentes")

# # Método capitalize() -> Retorna a 1ª letra maiúscula de uma palavra e o restante minúscula
# texto = 'exemplo teste'
# print(texto.capitalize())
# # Saída: Exemplo Teste

# data = input("Digite o dia, mês e ano qualquer: ")
# print(data.split('/'))                                     # A cada / ele separa como um item de uma lista
# # Saída: ['23', '09', '2024']

# texto = 'banana,uva,limão e morango'
# print(texto.split(','))                                     # A cada , ele separa como um item de uma lista
# # Saída: ['banana', 'uva', 'limão e morango']

# Método strip() -> remove espaço em branco do início ou do fim (NÃO ENTRE AS PALAVRAS)

# lstrip -> remove espaço da esquerda
# rstrip -> remove espaço da direita

# nome = '   Maria'
# print(nome.lstrip())
# # Saída: Maria

# nome = 'José  '
# print(nome.rstrip())
# # Saída: José

# Método replace() -> Substitui uma string por outra string

# frase = 'Texto exemplo'
# print(frase.replace('Texto', 'Teste'))   # Substitui a palavra Texto por Teste
# # Saída: Teste exemplo

frase = 'Curso de Programador de Sistemas'
print(frase.count('a')) 
print(frase.count('A'))
print(frase.upper().count('A'))

# count() -> retorna quantas caracteres iguais existem numa palavra

# info = input("Digite uma informação: ")
# print('A informação é do tipo: ', type(info)) # Tipo de dado (str, int, float, bool)
# print('A informação é um número? ', info.isnumeric()) # Número
# print('A informação é um alfabético? ', info.isalpha()) # Texto
# print('A informação é um alfanumérico? ', info.isalnum()) # Texto ou número
# print('A informação é um espaço? ', info.isspace()) # Espaço em branco
# print('A informação é captalizada? ', info.istitle()) # Texto com 1ª letra maiúscula
# print('A informação é maiúsculo? ', info.isupper()) # Texto inteiro em maiúsculo
# print('A informação é minúsculo? ', info.islower()) # Texto inteiro em minúsculo

# Pegando um caractere pelo índice (posição)
# caractere = 'Substrings em Python'
# print(caractere[0])  # Saída: S 
# print(caractere[5])  # Saída: r 
# print(caractere[19]) # Saída: n 
# print(caractere[20]) # Saída: IndexError: stringindex out of range 

nome = 'Python'
saldo = 100

print(f'Seu saldo é de \033[1;30;42m{saldo}\033[m reais')
