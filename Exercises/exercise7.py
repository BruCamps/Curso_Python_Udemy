"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ").strip()
numLetras = len(nome)
temEspacos = ' ' in nome

if nome:
    if not nome.isalpha():
        if temEspacos:
            print("[ERRO: Há mais de um valor]\n")
        else: 
            print("[ERRO: O nome deve conter apenas letras]\n")
    elif numLetras > 6:
        print(f"Seu nome é muito grande\n")
    elif numLetras >= 5:
        print(f"Seu nome é normal\n")
    elif numLetras > 0:
        print(f"Seu nome é curto\n")
else:
    print("[ERRO: Nenhum nome foi digitado]\n")
