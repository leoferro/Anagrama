import request

def criarAnagrama(palavra):
    num=len(palavra)
    l1=[]
    palavra=str(palavra)
    for x in palavra:
        l1+=[x]
    l2={palavra}
    for x in range(num):
        for y in range(num):
            prox=x+y+1
            if prox>=num:
                prox=prox%num
            troca=l1[prox]
            l1[prox]=l1[x]
            l1[x]=troca
            juntar=''.join(l1)
            l2.add(juntar)
    return(l2)

def encontrarAnagrama(palavras):
    listaDePalavras = []
    for palavra in palavras:
        encontrar =   request.retornaPalavra(palavra)
        if (encontrar):
            listaDePalavras.append(encontrar)
    return listaDePalavras


