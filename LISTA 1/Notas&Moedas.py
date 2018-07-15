#Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

valor = float(input(""))
resto = 0
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
moedas1 = 0
moedas50 = 0
moedas25 = 0
moedas10 = 0
moedas05 = 0
moedas01 = 0
if valor >= 100:
    notas100 = valor//100;
    valor = valor%100;
if valor >= 50:
    notas50 = valor//50;
    valor = valor%50;
if valor >= 20:
    notas20 = valor//20;
    valor = valor%20;
if valor >= 10:
    notas10 = valor//10;
    valor = valor%10;
if valor >= 5:
    notas5 = valor//5;
    valor = valor%5;
if valor >= 2:
    notas2 = valor//2;
    valor = valor%2;
if valor >= 1:
    moedas1 = valor//1;
    valor = valor%1;
if valor >= 0.5:
    moedas50 = valor//0.5;
    valor = valor%0.5;
if valor >= 0.25:
    moedas25 = valor//0.25;
    valor = valor%0.25;
if valor >= 0.10:
    moedas10 = valor//0.10;
    valor = valor%0.10;
if valor >= 0.05:
    moedas05 = valor//0.05;
    valor = valor%0.05;
if valor >= 0.01:
    moedas01 = valor//0.01;
    valor = valor%0.01;
    
notas100 = "%.0f" % notas100    
notas50 = "%.0f" % notas50     
notas20 = "%.0f" % notas20     
notas10 = "%.0f" % notas10     
notas5 = "%.0f" % notas5    
notas2 = "%.0f" % notas2    
moedas1 = "%.0f" % moedas1    
moedas50 = "%.0f" % moedas50    
moedas25 = "%.0f" % moedas25    
moedas10 = "%.0f" % moedas10   
moedas05 = "%.0f" % moedas05   
moedas01 = "%.0f" % moedas01

print("NOTAS:")    
print("{} nota(s) de R$ 100.00".format(notas100))    
print("{} nota(s) de R$ 50.00".format(notas50))    
print("{} nota(s) de R$ 20.00".format(notas20))    
print("{} nota(s) de R$ 10.00".format(notas10))    
print("{} nota(s) de R$ 5.00".format(notas5))    
print("{} nota(s) de R$ 2.00".format(notas2))
print("MOEDAS:")        
print("{} moeda(s) de R$ 1.00".format(moedas1))    
print("{} moeda(s) de R$ 0.50".format(moedas50))    
print("{} moeda(s) de R$ 0.25".format(moedas25))    
print("{} moeda(s) de R$ 0.10".format(moedas10))    
print("{} moeda(s) de R$ 0.05".format(moedas05))    
print("{} moeda(s) de R$ 0.01".format(moedas01))    
