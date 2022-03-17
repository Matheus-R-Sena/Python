resp = 1
while resp == 1:
    X = int(input())
    a=1
    b=2

    for i in range (1,X+1,1):
        if (i==1):
            print(1)
        if (i==2):
            print(2)
        if (i==3):
            c = (a*b)+1
            print(c)
        if i > 3:
            a = b
            b = c
            d = (a*b)+1
            c = d
            print(c)
    resp= int(input())
    
        
    
    
    
    
    
    