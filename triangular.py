numero = int(input())

if(numero <= 0):
    print("Falso")
    
divisor1 = 2
finalizador = 0

while(divisor1 < numero-1 and finalizador == 0):
    divisor2 = divisor1 + 1
    divisor3 = divisor1 + 2
    if(numero%divisor1 == 0 and numero%divisor2 == 0 and numero%divisor3 == 0 ):
        print("{} * {} * {} = {}".format(divisor1,divisor2,divisor3,numero))
        print("Verdadeiro")
        finalizador = 1
    else:
        divisor1 = divisor1 + 1

if(divisor1 >= numero-1 and numero >= 0):
    print("Falso")