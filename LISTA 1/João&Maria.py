#João e Maria estão querendo obter informações sobre os carros de sua cidade.
#Para isso eles pediram que você escrevesse um programa para ajudá-los. 
#Eles vão digitar informações de diferentes carros e quando quiserem parar a leitura vão digitar a resposta ‘n’ ou ‘N’.
#Para cada carro serão lidos o ano e a velocidade.
#O programa deve exibir a quantidade de carros, o carro mais novo e o mais rápido.

letra = input()
quantidade = 0
maior_ano = 0
maior_velocidade = 0
velocidade_media= 0
soma_velocidade = 0

if(letra == 'n'):
    print("zero")
else:
    while(letra == "s" and letra != "n"):
        ano = int(input())
        velocidade = float(input())
        if(ano > maior_ano):
            maior_ano = ano
        if(velocidade > maior_velocidade):
            maior_velocidade = velocidade
        soma_velocidade = velocidade + soma_velocidade
        quantidade = quantidade + 1
        letra = input()
    print("{}".format(maior_velocidade))
    print("{}".format(maior_ano))
    media = soma_velocidade/quantidade
    print("{}".format(media))
        



