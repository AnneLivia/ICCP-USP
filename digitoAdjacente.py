n = int(input("Digite um numero: "))

sim = 0

while(n):
	numero = n % 10
	copia = n % 100
	if(copia == numero):
		sim = 1
	
	n = n // 10
	
if(sim):
	print("sim")
else:
	print("nao")