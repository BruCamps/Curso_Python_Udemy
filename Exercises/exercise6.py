"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try: 
    hora = int(input("Infome a hora (de 0 a 23): "))
    if hora < 24:
        if hora >= 18:
            print("Boa noite! :)")
        elif hora >= 12:
            print("Boa tarde! :3")
        elif hora >= 0:
            print("Bom dia! :D")
    else:
        print("\n[ERRO: A hora deve estar entre 0 e 23]")
except ValueError:
    print("\n[ERRO: O valor deve ser um número inteiro]\n")
