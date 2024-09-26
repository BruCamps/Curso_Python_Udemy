"""
Exercício:

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade

Se nome e idade forem digitados:
Exiba:
Seu nome é {nome}
Seu nome invertido é {nome invertido}
Seu nome contém (ou não) espaços
Seu nome tem {n} letras
A primeira letra do seu nome é {letra}
A última letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

if nome and idade:
    print(f'\nSeu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome.replace(' ', ''))} letras')
    print(f'{' ' in nome and "Seu nome contém espaços" or "Seu nome NÃO contém espaços"}')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}\n')
else: 
    print("\nDesculpe, você deixou um ou mais campos vazios.\n")
