A = int(input())
B = int(input())
C = int(input())

if (A+B == C) or (A+C==B) or (B+C==A):
    print("soma")
    
elif (A*B == C) or (A*C==B) or (B*C==A):
    print("multi")
    
elif ((A+B+C)%2 == 0):
        print ("par")
else:
    print ("impar")
    
