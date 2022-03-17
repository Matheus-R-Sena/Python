n = int(input())
v = []
trocas = 0

for i in range (n):
    for j in range (5): #para coletar os elementos do vetor
        v.append(int(input()))
    for j in range (5): #para ordenar o vetor 
        for  k in range (4): 
            if v[k] > v[k+1]:
                t = v[k]
                v[k] = v[k+1]
                v[k+1] = t
                trocas = trocas + 1 #para contar quantas trocas esse vetor fez
    
    print(trocas)
    trocas = 0
    v = []
   

