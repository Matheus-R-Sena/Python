n = int(input())
P = [] #pares
I = [] #ímpares
V = [] #Vetor principal
t = 0

for i in range (n):
    V.append(int(input()))

for i in range(len(V)): #dividindo o vetor em 2 vetores menores (Par e Impar)
    if V[i]%2==0:
        P.append(V[i]) #dividindo para par
    else:
        I.append(V[i]) #dividindo para impar
V=[] #Zerando o Vetor principal 
        
for i in range(len(P)-1):    #Ordenando os pares
    for j in range(i+1,len(P)):
        if P[i] > P[j]:
            t = P[i]
            P[i] = P[j]
            P[j] = t

for i in range(len(I)-1):    #Ordenando os ímpares
    for j in range(i+1,len(I)):
        if I[i] < I[j]:
            t = I[i]
            I[i] = I[j]
            I[j] = t
            
for i in range (len(P)):
    V.append(P[i])
    
for i in range (len(I)):
    V.append(I[i])
    
print(V)
            
            

            
    
    