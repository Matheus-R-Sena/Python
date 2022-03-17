n = int(input())
mat  = []

for i in range (n):
    l = []
    for j in range(n):
        l.append(int(input()))
    mat.append(l)
inver = []
for i in range (n):
    inver.append(mat[i][i])
for i in range (n):
    mat[i][i] = mat[i][n - 1 - i]
for j in range (len(mat)):
    mat[j][n-1-j] = inver[j]
prin = []
for k in range (1):
    for i in range(n):
        prin.append(mat[k][n-1-i])
for k in range (1):
    for i in range (n):
        mat[k][i] = prin[i]
print('{}'.format(mat))
        