# Fazer um programa que lê N números inteiros do teclado, e no final informa se os números
# lidos estão ou não em ordem crescente.
# Vamos assumir que (pode acreditar):
# - N >= 2
# Dica: guarde sempre o número anterior fornecido.
# ENTRADA: número inteiro N, seguido de N números inteiros
# SAIDA: “sim” se os números estão em ordem crescente e “não” caso contrário


N = int(input())
cont = 2
crescente = "sim"
num1 = int(input())
while cont <=N:
    num2 = int(input())
    cont = cont + 1
    if num1 <= num2:
        num1 = num2
    else:
        num1 = num2
        crescente = "não"
print(crescente)