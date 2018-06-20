n = 1
num = [ ]
while n != 0:
    n = int(input("Digite um valor terminado em 0: "))
    num.append(n)

tam = len(num) - 1
while(tam >= 0):
    print(num[tam])
    tam -=1
