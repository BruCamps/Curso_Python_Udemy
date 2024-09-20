"""
  Formatação de String por F-Strings:
 
  [Caractere(s)] [><^][quantidade)
  _______________________
  <  preenche à esquerda
  >  preenche à direita
  ^  centraliza
  _______________________

  ,.[número]f -> A vírgula separa as classes de números (Não muito usado)
  +.[número]f -> O sinal de + é mostrado caso o número seja positivo
  -.[número]f -> O sinal de - é mostrado caso o número seja negativo
  0=+[número].[número]f -> O sinal de = força o sinal de + a aparecer antes dos zeros
  
"""

variavel = 'ABC'             # Variável (string) que possui 3 caracteres
print(f'\n{variavel}')       # Imprime a variável
print(f'{variavel: >10}')    # Preenche com 7 caracteres de espaços em branco à esquerda até completar 10 caracteres
print(f'{variavel: <10}.')   # Preenche com 7 caracteres de espaços em branco à direita até completar 10 caracteres
print(f'{variavel: ^10}')    # Busca dividir os caracteres de espaços em branco em 2 partes para centralizar a variável
print(f'{variavel:*^10}\n')  # Busca dividir os caracteres de * em 2 partes para centralizar a variável

# ,.[número]f
numero = 123456.789
print(f'{numero:,.2f}')
# Saída: 123,456.79

# +.[número]f 
numero = 123456.789
print(f'{numero:+,.2f}')
# Saída: +123456.79

# -.[número]f 
numero = -123456.789
print(f'{numero:-,.2f}')
# Saída: -123456.79

# 0=+[número].[número]f
print(f'{1000.789034939403309:0=+10,.1f}')
# Saída: 000+1000.8 (Sem o sinal de =)
# Saída: +0001000.8 (Com o sinal de =)

# Exemplo do Hexadecimal com F-String 
print(f'O hexadecimal de 1500 é {1500:08X}')
