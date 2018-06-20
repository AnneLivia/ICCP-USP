def primo(n):
    i = 1
    cont = 0
    while(i <= n):
        if(n % i == 0):
            cont = cont + 1
        i = i + 1
    if(cont == 2):
        return n
    else:
        return 0
        
def maior_primo(x):
    if x < 2:
        return "Erro"
    i = 1
    while(i <= x):
        if(primo(i) != 0):
            max_primo = primo(i)
        i = i +1

    return max_primo

print(maior_primo(0))
