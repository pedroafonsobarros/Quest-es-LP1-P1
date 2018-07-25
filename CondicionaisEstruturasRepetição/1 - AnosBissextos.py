anoInicial = -1
anoFinal = -1
while anoInicial < 0 or anoFinal < 0:
	anoInicial = int(input("Digite o ano inicial: "))
	anoFinal = int(input("Digite o ano final: "))
	if anoInicial < 0 or anoFinal < 0:
		print("\n Digite apenas números maiores que 0!")

cont = anoInicial

while(cont <= anoFinal):
	if(cont % 4 == 0):
		print(cont)
	cont = cont + 1