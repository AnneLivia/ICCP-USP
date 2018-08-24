import re


def main():
    ass_input = le_assinatura()
    textos = le_textos()    
    cohpiah = avalia_textos(textos,ass_input)
    print("O autor do texto",cohpiah,"está infectado com COH-PIAH")
    

def le_assinatura():
    
    print("Bem-vindo ao detector automático de COH-PIAH.")

    tp = float(input("Entre o tamanho medio de palavra:"))
    tt = float(input("Entre a relação Type-Token:"))
    hl = float(input("Entre a Razão Hapax Legomana:"))
    ts = float(input("Entre o tamanho médio de sentença:"))
    cm = float(input("Entre a complexidade média da sentença:"))
    tf = float(input("Entre o tamanho medio de frase:"))

    return [tp, tt, hl, ts, cm, tf]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + "(aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + "(aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """
    A funcao recebe um texto e devolve uma lista das sentencas dentro
    do texto.
    """
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """
    A funcao recebe uma sentenca e devolve uma lista das frases dentro
    da sentenca.
    """
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """
    A funcao recebe uma frase e devolve uma lista das palavras dentro
    da frase.
    """
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """
    Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    que aparecem uma unica vez.
    """
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """
    Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas.
    """
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

""" Função responsável por calcular a quantidade de palavras """
def qtd_palavras(texto):
    listSent = separa_sentencas(texto) 
    qtdPalavras = 0
    for i in listSent:
        listFrase = separa_frases(i)
        for j in listFrase:
            listaPalavra = separa_palavras(j) 
            qtdPalavras+=len(listaPalavra) 
    return qtdPalavras
    
""" Função responsavel por somar o tamanho das palavras """
def soma_tamanho(texto):
    soma = 0
    listSent = separa_sentencas(texto)
    for i in listSent:
        listFrase = separa_frases(i)
        for j in listFrase:
            listaPalavra = separa_palavras(j)
            for k in listaPalavra:
                soma = soma + len(k)
    return soma

""" Função para calcular o tamanho medio de palavras, onde o tamanho medio se da
pela soma dos tamanhos das palavras dividido pelo numero total de palavras"""
def tamanho_medio(texto):
    qtdPalavras = qtd_palavras(texto)
    somaTamanhos = soma_tamanho(texto)

    if(qtdPalavras != 0):
        return somaTamanhos/qtdPalavras
    else:
        return 0

""" Função responsável por cacular a relação type token, no qual se é calculado o número de palavras diferentes dividido pelo total de palavras"""
def relacao_type_token(texto):
    listSent = separa_sentencas(texto)
    qtdPalavrasDiferentes = 0
    listWord = []
    for i in listSent:
        listFrase = separa_frases(i)
        for j in listFrase:
            listWords = separa_palavras(j)
            for k in listWords:
                listWord.append(k)


    qtdPalavrasDiferentes += n_palavras_diferentes(listWord)
    
    qtdPalavras = qtd_palavras(texto)
    if qtdPalavras != 0:
        return (qtdPalavrasDiferentes/qtdPalavras)
    else:
        return 0

""" Função responsável por calcular a razão hapax legomana onde se é feito pelo número de palavras
que aparecem uma unica vez dividido pelo total de palavras """
def razao_hapax_legomana(texto):
    listSent = separa_sentencas(texto)
    
    listWord = []

    for i in listSent:
        listFrase = separa_frases(i)
        for j in listFrase:
            listWords = separa_palavras(j)
            for k in listWords:
                listWord.append(k)

    qtdPalavrasUnicas = n_palavras_unicas(listWord)
    qtdPalavras = qtd_palavras(texto)
    if(qtdPalavras != 0):
        return (qtdPalavrasUnicas/qtdPalavras)
    else:
        return 0


""" Função responsável por calcular o tamanho medio de sentença, onde é a soma dos número de caracteres
em toda a sentença dividida pelo número de sentenças"""
def tamanho_medio_sentenca(texto):
    listsent = separa_sentencas(texto)
    qtdSentecas = len(listsent)
    somaCarac = 0
    for i in listsent:
        somaCarac+=len(i)
    if qtdSentecas != 0:
        return (somaCarac/qtdSentecas)
    else:
        return 0

""" Função que calcula a complexidade de setença onde se é dado pelo total de frases dividido pelo numero de sentecas"""
def complexidade_setenca(texto):
    listSent = separa_sentencas(texto)
    qtdFrases = 0
    qtdSentecas = len(listSent)
    for i in listSent:
        qtdFrases += len(separa_frases(i))
    return (qtdFrases/qtdSentecas)

""" Tamanho médio de frase: soma do número de caracteres em cada frase dividida pelo número de frases no texto"""
def tamanho_medio_frase(texto):
    qtdFrases = 0
    qtdCarac = 0
    listSent = separa_sentencas(texto)
    for i in listSent:
        listFrases = separa_frases(i)
        qtdFrases+=len(listFrases)
        for j in listFrases:
            qtdCarac+=len(j)
            
    return (qtdCarac/qtdFrases)


def calcula_assinatura(texto):
    """
    Essa funcao recebe um texto e deve devolver a assinatura
    do texto.
    """
    ass_main = []
    tm = tamanho_medio(texto)
    rl = relacao_type_token(texto)
    rhl = razao_hapax_legomana(texto)
    tms = tamanho_medio_sentenca(texto)
    compl = complexidade_setenca(texto)
    tmf = tamanho_medio_frase(texto)

    ass_main.append(tm)
    ass_main.append(rl)
    ass_main.append(rhl)
    ass_main.append(tms)
    ass_main.append(compl)
    ass_main.append(tmf)
    return ass_main


def compara_assinatura(ass_main, matriz_ass_input):
    """
    Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.
    """
    grau_similaridade = 0
    
    for i in range(0, 6):
        grau_similaridade+=(abs(ass_main[i] - matriz_ass_input[i]))
    
    resultado = grau_similaridade / 6.0
    return resultado
    


def avalia_textos(textos_main, ass_comparadas):
    """
    Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    """
    list_infectados = []
    for i in textos_main:
        ass = calcula_assinatura(i)
        simi = compara_assinatura(ass,ass_comparadas)
        list_infectados.append(simi)
    
    menor = 0
    
    for i in range(1, len(textos_main)):
        
        if list_infectados[menor] >= list_infectados[i]:
            menor = i
    return menor + 1
    
main()
    
