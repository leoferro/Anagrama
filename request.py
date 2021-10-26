import requests

def retornaPalavra(palavra):
    url= 'https://api.dicionario-aberto.net/word/'+palavra
    res = requests.get(url)
    data = res.json()
    if len(data)>0:
        return res.json()[0]['word']
    else:
        return False