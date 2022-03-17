n = int(input())

# Montando A
A = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input()))
    A.append(l)
# Montando B multiplicando AXA    
B = []
for i in range(n):
    B.append([0]*n)
    
for i in range(n):
    for j in range(n):
        pe = 0
        for k in range(n):
            pe = pe + A[i][k]*A[k][j]
        B[i][j] = pe
# Fazendo a transposta de A
tam = (n*n)
V = [0]*(tam)
# Trocando a matriz de A por um vetor
ind=0
for i in range(n):
    for j in range(n):
        V[ind]=A[i][j]
        ind =ind+1
        
ind=0
# Invertendo linhas por colunas
for i in range(n):
    for j in range(n):
        A[j][i] = V[ind]
        ind = ind+1

#Somando a matriz transposta de A com B

# Trocando a matriz de A por um vetor
ind=0
VA = [0]*(tam)
for i in range(n):
    for j in range(n):
        VA[ind]=A[i][j]
        ind =ind+1

# Trocando a matriz de B por um vetor
ind=0
VB = [0]*(tam)
for i in range(n):
    for j in range(n):
        VB[ind]=B[i][j]
        ind =ind+1
# Somando os 2 Vetores

VS = [0]*(tam)
for i in range (tam):
    VS[i] = VA[i] + VB[i]
#Transformando VS em uma matriz


# Inserindo em C    
C = []
soma = 0
for i in range(n):
    l = []
    for j in range(n):
        l.append(VS[soma])
        soma = soma + 1
    C.append(l)
print(C)

        
