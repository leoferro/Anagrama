import arrumando_listas 
import palavras
def anagrama(palavra):
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

def arquivoparalista(arquivo):
    arq=open(arquivo, 'r')
    palavras=[]
    for x in arq:
       palavras+=[arq.readlines()]
    arq.close()
    return palavras

def encontraranagrama(anagrama, lista):
    palavrasexistentes=[]
    for x in anagrama:
        if x in lista:
            palavrasexistentes+=[x]
    return palavrasexistentes

#lista ja foi transformada em lista no final

l1=arrumando_listas.stremlista(palavras.lista)
lista=arrumando_listas.arrumandopalavras(l1)

