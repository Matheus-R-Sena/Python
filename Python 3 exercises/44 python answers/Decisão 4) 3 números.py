A = int(input())
B = int(input())
C = int(input())

if (A==B) and (A!=C):
    print(C)
    
elif (A!=B) and (B!=C) and (C!=A):
    print(A+B+C)
    
elif (A!=B) and (B==C):
    print(A)

elif (A!=B) and (B!=C) and (A==C):
    print(B)
else:
    print(0)