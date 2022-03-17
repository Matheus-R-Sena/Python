valor = int(input())

if (valor >= 100):
    if (valor%100 == 0) or (valor%100 != 0):
        A = valor//100
        valor = valor%100 
        print('%.0f'%A," de 1r")
        
        
if (valor >= 50) and (valor < 100):
     if (valor%50 == 0) or (valor%50 != 0):
         B = valor//50
         valor = valor%50
         print('%.0f'%B," de 50c")
         
         
if (valor >= 25) and (valor < 50):
    if (valor%25 == 0) or (valor%25 != 0):
        C = valor//25
        valor = valor%25
        print('%.0f'%C," de 25c")
   
if (valor%1 == 0) and (valor<25) and (valor!=0):
    D=valor/1
    print('%.0f'%D," de 1c")
    
    