a = int(input())
b = int(input())
c = int(input())
d = int(input())
#letras são os números de tomadas em cada regua dadas pelo ususário
Numero_maximo_aparelhos = (a+b+c+d)-3
#menos 3 porque levando em conta que uma regua se conecta na outra em 3 reguas perderemos 1 tomada

print(Numero_maximo_aparelhos)
