tamanho = int(input("Quantos números vão ser digitados? \n"))
vetor = []
cont = 0
soma = 0
pares = 0
print("Digite os números:\n")
for cont in range(tamanho):
	vetor[cont] = int(input())
	if(vetor[cont] >= 0 and vetor[cont] % 2 == 0):
		soma = soma + vetor[cont]
		pares = pares + 1
if pares == 0:
	print(-1)
else:
	media = soma/pares
	print(media)
