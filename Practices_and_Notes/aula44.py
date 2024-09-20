"""
  Formatação de Strings por Interpolação usando %:
  %s      -> string
  %d e %i -> inteiro
  %f      -> float
  %e e %E -> float em notação científica
  %x e %X -> hexadecimal 

  DICA: %x gera letras minúsculas e %X gera letras maiúsculas
  
"""

nome = 'Joaquim'
preco = 1000.97893257
mensagem = f'%s comprou um item que custou R$%.2f' % (nome, preco)
print(mensagem)

print('O Hexadecimal de %d é %04x' % (15, 15))

"""
  DICA: Preencher com zeros a esquerda:
  print('O Hexadecimal de %d é %04x' % (15, 15))  
  
  # '%04' representa a quantidade de dígitos desejada e caso não haja 4 dígitos será preenchido 
  # com zeros a esquerda
  
  # Saída: O Hexadecimal de 15 é 000f

"""
print('O Hexadecimal de %d é %08X' % (1500, 1500))
# Saída: O Hexadecimal de 1500 é 000005DC

# OBS.: O hexadecimal de 1500 é 5DC, mas como só tem apenas 3 digitos, e colocamos que precisamos de 8 digitos no total, os outros 5 são preenchidos com zeros a esquerda
