import math
A=[]
Mo=[]
S = 0
me = 0


for i in range (5):
    A.append(float(input())) #Formar a lista dos números reais
    
for i in range (len(A)): #Calcular a soma deles
    S = S + A[i]
    
Media = S/5 #Calcular a média deles

for i in range (len(A)): #Criar uma lista com a diferença dos números (Mo)
    M = A[i] - Media
    Mo.append(math.fabs(M))
    
for i in range (len(Mo)): #Para encontrarmos o menor valor dessa lista
    if i == 0:
        me = Mo[0]
    if Mo[i] < me:
        me = Mo[i]
        Me = A[i] # número mais próximo
        
if Mo[0] - me == 0:
    print('%.2f'%A[0])
else:
    print('%.2f'%Me)
    