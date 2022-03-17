numero = int(input())
d5= numero//1 % 10
d4= numero//10 % 10
d3= numero//100 % 10
d2= numero//1000 % 10
d1= numero//10000 % 10

if (d5 == d1) and (d4 == d2):
    print("sim")
else:
    print("não")
    
