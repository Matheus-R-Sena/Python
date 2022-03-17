n = int(input())
X = 0
Y = 0
Z = 0
triangular = 0
for i in range (2,n+1,1):
    A = i
    B = i+1
    C= i +2
    if A*B*C == n:
        X = A
        Y = B
        Z = C
        triangular = n
        break
if X*Y*Z == triangular and X*Y*Z!=0:
    print(A)
    print(B)
    print(C)
else:
    print("não")
            
        
   