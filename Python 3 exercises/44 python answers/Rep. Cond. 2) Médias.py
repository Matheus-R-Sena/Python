X = int(input()) #Quantidade de alunos
NA = 0          
mediaS= 0

while NA!=X:
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + nota2)/2
    mediaS = media + mediaS
    NA = NA + 1
print('%.2f'%mediaS)

