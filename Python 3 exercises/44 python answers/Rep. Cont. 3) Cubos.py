for i in range (100,1000,1):
    n3 = i//1 %10
    n2 = i//10 %10
    n1 = i//100 %10
    if (n1**3)+(n2**3)+(n3**3) == i:
        print(i)