cor = str(input())
A = "Amarelo"
E = "Vermelho"
V = "Verde"
Z = "Azul"

if ( cor == V):
    cor = "10,00"
    print("Custo R$",cor)
elif (cor == A):
    cor = "30,00"
    print ("Custo R$",cor)
elif (cor == E):
    cor = "40,00"
    print("Custo R$",cor)
else:
    if(cor == Z):
        cor = "20,00"
        print("Custo R$",cor)