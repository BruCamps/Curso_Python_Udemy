"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = input("Digite um número inteiro: ")
    if num:
        print(f"O número {num} é {int(num) % 2 == 0 and 'par' or 'ímpar'}")
    else:
        print("[Nenhum valor inserido]\n")
except ValueError:
    print("[ERRO: O valor informado não é um número inteiro]\n")
