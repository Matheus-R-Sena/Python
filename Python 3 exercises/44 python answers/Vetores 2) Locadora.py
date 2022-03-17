A = 0
LG = [] #locações gratuitas
C = [] #Locações por clientes

for i in range (10):
    C.append(int(input()))
for i in range (10):
    if (C[i]%5 > 0 or C[i]%5 == 0) and C[i] >= 5:
        A = C[i]%5      #Resto da divisão
        B = (C[i]-A)/5  #Divisão sem o resto(para saber quantos o cliente tem direito)    
        LG.append(int(B))
    else:
        LG.append(int(0))
print(LG)