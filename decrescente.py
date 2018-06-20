valor = 1
decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

while valor != 0 and decrescente:
	valor = int(input("Digite o proximo valor da sequência: "))
	if valor > anterior:
		decrescente = False
	anterior = valor
	
if decrescente:
	print("Está em ordem decrescente :) ")
else:
	print("Não está em ordem decrescente :( ")