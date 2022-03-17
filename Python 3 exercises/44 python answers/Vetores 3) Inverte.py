N = int(input())#Número de elementos na lista A
A = []
Ai = []   #A invertido
B = []
f = 1
for i in range(N):
    A.append(int(input()))
    
for j in range (len(A)):
    Ai = [A[j]] + Ai
    
for K in range (len(Ai)):

    H = Ai[K]
    if H>=0 :
        for M in range (1,H+1,1):    
            f = f*M
        Ai[K] = f
        f = 1
        B = B + [Ai[K]]
    else:
        B = B + [Ai[K]]
print(B)
    
# 5
# -2
# 7
# 3
# 0
# 5
        
  
