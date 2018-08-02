pessoas = []
i = 0
pesoTotal = 0
parada = False

while pessoas[i] != 0 and i <= 7 and parada == False:
	pessoas[i] = int(input(""))
	i = i + 1
	pesoTotal = pesoTotal + pessoas[i]
	if pesoTotal > 560:
		pesoTotal = pesoTotal - pessoas[i]
		parada = True

print(i)
print(pesoTotal)
