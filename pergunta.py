import anagrama
x=input('qual palavra\n')
print('Os anagramas existentes são:\n',anagrama.encontraranagrama(anagrama.anagrama(x),anagrama.lista),'\nTodos são:\n',anagrama.anagrama(x))
