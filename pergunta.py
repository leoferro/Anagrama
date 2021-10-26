from anagrama import criarAnagrama, encontrarAnagrama

palavra=input('qual palavra\n')

anagramas = criarAnagrama(palavra)
encontros =  encontrarAnagrama(anagramas)

print('Os anagramas existentes são:\n',', '.join(encontros),'\nTodos são:\n',', '.join(anagramas))
