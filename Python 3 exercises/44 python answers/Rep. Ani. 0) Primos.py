A = int(input())
B = int(input())
C = 0

for i in range (A, B+1,1):
    for z in range(2,i+1,1):
        if i%z==0 and i!=z:
            C = 1
    if C ==0:
        print(i)
    C = 0
            