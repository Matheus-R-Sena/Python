X = int(input())
a = 3
b = 7
Soma = 0


for i in range (99):
     if (i % 2 == 0):
         Soma   = Soma + (a*X / b)
     else:
         Soma = Soma - (a*X/b)
     a = a + 5
     b = b + 2
SomaT = Soma+X
print(float('%.3f'%SomaT))
         

