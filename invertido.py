n = int(input())
tam = len(str(n))
count = 0
invertido = 0
v = 0

while tam >= 1:
    tam = tam - 1
    pow = 10**tam
    v = int(n/pow)
    invertido = invertido + v*(10**count)
    n = n%pow
    count = count + 1
print(invertido)