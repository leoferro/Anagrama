from unidecode import unidecode
def stremlista(string):
    lista=[]
    x=0
    y=0
    while True:
        x=string.find('\n', y)
        if x==-1:break
        lista+=[string[y:x]]
        y=x+1
    return lista

def arrumandopalavras(lista):
    novalista=[]
    for palavra in lista:
        palavra=unidecode(palavra).lower()
        if palavra.find('/')!=-1:
            palavra=palavra[:palavra.find('/')]
        novalista+=[palavra]
    return novalista


