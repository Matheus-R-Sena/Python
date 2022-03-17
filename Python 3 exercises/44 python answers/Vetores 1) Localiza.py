A = []
B = []

for i in range (10):
    A.append(int(input()))
U = int(input())

for j in range (len(A)):
    if A[j] == U:
        B.append(j)
print(B)


