vetor1 = 0
vetor2 = 0
intersec = 0
cont = 0
n = 0
aux =0
while cont < 40:
    if(cont<20):
        vetor1[cont] = int(input())
    else:
        vetor2[cont] = int(input())
        for n in range(20-1):
            if vetor2[cont] == vetor1[n]:
                intersec[aux] == vetor2[cont]
                aux = aux+1
    cont = cont + 1
n = 0
for n in range(aux-1):
    print("{}".format(intersec[n]))