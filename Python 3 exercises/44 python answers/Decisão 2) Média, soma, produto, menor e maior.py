A = int(input())
B = int(input())
C = int(input())

media = (A+B+C)/3
print('%.1f'%media)

soma = A+B+C
print(soma)

produto = A*B*C
print(produto)

if(A<B) and (A<C):
    print(A)
else:
    if(B<C):
        print(B)
    else:
        print(C)

if(A>B) and (A>C):
    print(A)
else:
    if(B>C):
        print(B)
    else:
        print(C)