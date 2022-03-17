n = int(input())
matricula = []
nota = []

for i in range(n):
    matricula.append(int(input()))
for i in range(n):
    nota.append(float(input()))

for i in range (n-1):
    for j in range (i+1, n):
        if nota[i] > nota[j]:
            t = matricula[i]
            matricula[i] = matricula[j]
            matricula[j] = t
print(matricula)