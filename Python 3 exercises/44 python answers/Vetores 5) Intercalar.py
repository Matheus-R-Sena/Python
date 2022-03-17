A = []
B = []

N = int(input())
M = int(input())


for i in range (N):
    A.append(int(input()))
    
for i in range (M):
    B.append(int(input()))
    
C = []

for i in range (N + M):
    if (N > i):
        C.append(int(A[i]))
    if (M > i):
        C.append(int(B[i]))
        
print(C)
    