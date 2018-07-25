tamanhoI = 45
tamanhoII = 30

p1 = []
p2 = []

cont = 0
for cont in range[tamanhoI]:
	p1[cont] = int(input(""))

cont =0
for cont in range[tamanhoII]:
	p2[cont] = int(input(""))

cont = 0
i = 0

for cont in range[tamanhoII]:
	for i in range[tamanhoI]:
		if p2[cont] == p1[i]:
			print(p2[cont])

print("Deu certo")