# Exercício: Utilize condicionais (if e else) e operadores relacionais para fazer com que 
# o número maior seja exibido primeiro e o menor número em seguida.  

# Modelo:
# segundo_valor='2' é maior do que primeiro_valor='1'

primeiro_valor = input('\nDigite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor >= segundo_valor:  # Verifica se o primeiro valor é maior ou igual ao segundo
  print(f'\nO {primeiro_valor=} é maior do que o {segundo_valor=}\n')
else:
  print(f'\nO {segundo_valor=} é maior do que o {primeiro_valor=}\n')
