X = int(input())#número de pokemons de A
Y = int(input())#número de pokemons de B
A = 50/100
B = 30/100
anos=0

while X < Y:
    CrescimentoA = int(X*A)#Para o Jogador A
    X = CrescimentoA + X
    
    CrescimentoB = int(Y*B)#Para o Jogador B
    Y = CrescimentoB + Y
    
    anos = anos + 1
print(anos)
    
    
    
    
    
    