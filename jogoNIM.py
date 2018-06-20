vitoriasC = 0
vitoriasU = 0

def computador_escolhe_jogada(n,m):
	quantidade = 0
	while(( n - quantidade ) % (m+1) != 0 and (n - quantidade) > 0 and quantidade <= m):
			quantidade = quantidade + 1
	if((n - quantidade) % (m+1) == 0 and quantidade <= m):
		return quantidade
	else:
		return m
		
def usuario_escolhe_jogada(n,m):
	quantUsuario = 0
	while(quantUsuario > m or quantUsuario < 1 or quantUsuario > n):
		if(quantUsuario != 0):
			print("Ops, jogada invalida! Rente de novo.")
		quantUsuario = int(input("Quantas peças você vai retirar: "))
	print("\n")
	return quantUsuario
	
def partida():
	n = 0
	m = 0
	teste = 0
	while(n <= 0 or m <= 0):
		if(teste == 1):
			print("Quantidade de palitos invalida")
		n = int(input("Informe a quantidade de peças: "))
		m = int(input("Infome o limite de peças por jogada: "))
		teste = 1
		
		
	print("\n")
	if(n % (m+1) == 0):                                 #Se a quantidade de peças for multiplo de m + 1, o jogador começa
		print("Você começa!")
		while(n > 0):                                   #Enquanto a quantidade de peças for maior que 0 o loop é execultado
			vez = 2 									#Vez = 2 significa que é a vez do usuario
			
			Qpeca = usuario_escolhe_jogada(n,m)			#Vez do jogador jogar, chamando a função
			if(Qpeca == 1):
				print("Você tirou uma peça do tabuleiro")
			else:
				print("Você tirou",Qpeca,"peças do tabuleiros")
			n = n - Qpeca								#Removendo as peças retiradas
			fim = quantidadePecas(n,vez)				#escrevendo quantidade de peças no jogo e caso seja 0 será retornado para fim, 1
			if(fim):
				return 0								#Caso fim seja 1, será o fim da função partida						
			vez = 1										#Vez = 1 significa que é a vez do computador
			
			Qpeca = computador_escolhe_jogada(n,m)
			if(Qpeca == 1):
				print("O Computador tirou uma peça do tabuleiro")
			else:
				print("O computador tirou",Qpeca,"peças do tabuleiros")
			n = n - Qpeca                               
			fim = quantidadePecas(n,vez)
			if(fim):
				return 0
		
	else:
		print("Computador começa!\n")
		while(n > 0):
			vez = 1
			Qpeca = computador_escolhe_jogada(n,m)     
			if(Qpeca == 1):
				print("O Computador tirou uma peça do tabuleiro")
			else:
				print("O computador tirou",Qpeca,"peças do tabuleiros")
			n = n - Qpeca
			fim = quantidadePecas(n,vez)
			if(fim):
				return 0
			
			vez = 2
			Qpeca = usuario_escolhe_jogada(n,m)
			if(Qpeca == 1):
				print("Você tirou uma peça do tabuleiro")
			else:
				print("Você tirou",Qpeca,"peças do tabuleiros")
			n = n - Qpeca
			fim = quantidadePecas(n,vez)
			if(fim):
				return 0
			
def campeonato():
	global vitoriasC, vitoriasU
	rodada = 1
	while(rodada <= 3):
		print("\n **** Rodada",rodada,"****\n")
		partida()
		rodada = rodada + 1
	print("Placar: Você",vitoriasU,"X",vitoriasC,"Computador")
	print("\n**** Final do campeonato! ****")
	
def printPecas(n):
	if(n == 1):
		print("Agora resta uma peça no tabuleiro\n")
	else:
		print("Agora restam",n,"peças no tabuleiro\n")
		
def quantidadePecas(n,vez):
	global vitoriasC,vitoriasU 	
	if(vez == 1):
		if(n == 0):
			print("Fim de jogo, O Computador ganhou\n")
			vitoriasC = vitoriasC + 1
			return 1
		else:
			printPecas(n)
	else:
		if(n == 0):
			print("Fim de jogo, Você ganhou\n")
			vitoriasU = vitoriasU + 1
			return 1
		else:
			printPecas(n)
			
def jogo():
	print("Bem vindo ao jogo do NIM, escolha:")
	print("1 - para jogar uma partida isolada")
	print("2 - para jogar um campeonato")
	op = int(input())
	if(op == 1):
		partida()
	else:
		campeonato()
	
jogo()
