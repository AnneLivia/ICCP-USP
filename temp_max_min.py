def temperaturas(temps):
    print("A menor temperatura é: ",minimo(temps),"C.")
    print("A maior temperatura é: ",maximo(temps),"C.")


def minimo(temps):
    min = temps[0]
    i = 0
    while(i < len(temps)):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min


def maximo(temps):
    max = temps[0]
    i = 0
    while(i < len(temps)):
        if  max < temps[i]:
            max = temps[i]
        i = i + 1
    return max


def is_empty(inicio):
    if inicio != 0:
        return 1
    print("Banco de dados com as têmperaturas está vázio!")
    return 0

def menu():
    opc = 1
    inicio = 0
    temps = []
    while opc != 5:
        print("---------------- MENU ------------------")
        print("1 - Inserir têmperaturas de uma quantidade de meses\n"
                "2 - Listar as têmperaturas já inseridas\n"
                "3 - Veriricar as menores e as maiores têmperaturas do banco de dados de têmperaturas\n"
                "4 - Zerar os dados já armazenados\n"
                "5 - sair")
        opc = int(input("Digite aqui: "))
        if opc == 1:
                temps = valores_temp(temps)
                inicio = 1
        elif opc == 2 and is_empty(inicio):
                listar_temps(temps)
        elif opc == 3 and is_empty(inicio):
                    temperaturas(temps)
        elif opc == 4:
            print("Banco de dados com as têmperaturas está zerado!")
            temps = []
            inicio = 0
        elif opc == 5:
                print("Programa finalizado!")
        else:
                print("Opção invalida!")

                    
def valores_temp(temps):
    quant = int(input("Quantos meses foram registrados as temperaturas ? "))
    for i in range(quant):
         print("Mês",i+1,":",end="")
         valor = int(input("Qual temperatura  ? "))
         temps.append(valor)
    return temps


def listar_temps(temps):
        for i in range(len(temps)):
            print("Mês",i+1,":",temps[i],"C.")


        
def teste_pontualMax(temps,valor_esperado):
    max = maximo(temps)
    if max != valor_esperado:
        print("Valor maximo errado para",temps)
        print("O valor deveria ser:",valor_esperado,"e foi:",max)

def teste_maximo():
   teste_pontualMax([0],0)
   teste_pontualMax([0,0,0,0],0)
   teste_pontualMax([20,21,23,22,121,32,44],121)
   teste_pontualMax([-12,-12,-14,-223,-121],-12)


def teste_pontualMin(temps,valor_esperado):
    min = minimo(temps)
    if min != valor_esperado:
        print("Valor minimo errado para",temps)
        print("O valor deveria ser:",valor_esperado,"e foi:",min)
    
def teste_minimo():
   teste_pontualMin([0],0)
   teste_pontualMin([0,0,0,0],0)
   teste_pontualMin([20,21,23,22,121,32,44],20)
   teste_pontualMin([-12,-12,-14,-223,-121],-223)

