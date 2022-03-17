n = int(input())
m = int(input())

s = float(0)

for i in range(1,n+1):
    for j in range (1,m+1):
        s = s + (i**2) * j/((3**i) * (j * (3**i) + i * (3**j)))
print("%.4f"%s)