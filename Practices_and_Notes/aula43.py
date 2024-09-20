"""
  O operador (in) verifica se 1 ou + caracteres estão em uma string.
  O operador (not in) verifica se 1 ou + caracteres não está em uma string.
"""

nome = 'Otávio'

"""
  Índices (+)    0 1 2 3 4 5 
  String         O t á v i o
  Índices (-)   -6-5-4-3-2-1
"""

print(nome[2]) # Imprime (exibe) o caractere 'á' na posição 2
print(nome[-3]) # Imprime (exibe) o caractere 'v' na posição -4

# Utilizando os operadores (in) e (not in)
print('vio' in nome)      # Verifica se 'vio' está em (in) nome
print('z' in nome)        # Verifica se 'z' está em (in) nome
print(10 * '-') 
print('z' not in nome)    # Verifica se 'z' não está em (not in) nome
print('vio' not in nome)  # Verifica se 'vio' não está em (not in) nome

# Atividade Prática
# -> Crie um programa que verifique se 1 ou + caracteres estão em uma string

nomePessoa = input('Digite seu nome: ')
encontrar = input('Verifique se o(s) caractere(s) que digitar estão em seu nome: ')

if encontrar in nomePessoa: # Verifica se a palavra digitada em 'encontrar' está em 'nomePessoa'
  print(f'\n[{encontrar} está em {nomePessoa}]\n')
else:
  print(f'\n[{encontrar} não está em {nomePessoa}]\n')
