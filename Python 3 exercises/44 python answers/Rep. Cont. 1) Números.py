n = int(input())
n2 = n
n3 = int(0)
maior = int(0)
menor = int(100)
soma = int(0)
produto = int(1)
media = float(0)

for i in range (n):
    n3 = int(input())
    soma = soma + n3
    produto = produto * n3
    
    if (n3 > maior):
        maior = n3
    else:
        maior = maior
    
    if (n3 < menor):
        menor = n3
    else:
        menor = menor
media = float(soma / n2)
print("%.2f" %media)
print(soma)
print(produto)
print(menor)
print(maior)