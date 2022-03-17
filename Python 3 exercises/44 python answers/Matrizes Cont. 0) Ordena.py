n = int(input())
m = int(input())

tam = (n*m)
V = [0]*(tam)

A = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(int(input()))
    A.append(l)


ind=0
for i in range(n):
    for j in range(m):
        V[ind]=A[i][j]
        ind =ind+1


for i in range(tam):
    for j in range(tam-1):
        if (V[j]<V[j+1]):
            t = V[j]
            V[j] = V[j+1]
            V[j+1] = t


ind=0
for i in range(m):
    for j in range(n):
        A[j][i] = V[ind]
        ind = ind+1

print(A)