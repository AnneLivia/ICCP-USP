n = int(input("Digite um número: "))

i = 2
cont = 1

while(i <= n):
	if(not(n % i)):
		cont +=1
	i+=1

if(cont == 2):
	print("primo")
else:	
	print("não primo")