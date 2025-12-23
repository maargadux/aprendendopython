algo = input('digite algo: ')

'primitivos = são tipos de dados primitivos(básicos), ou seja tipos de dados que podemos manipular dentro de uma variavel'
'ele localiza o type de variavel automaticamente'

print('caralho voce disse:"', algo,'" voce sabia que o que voce disse faz parte do tipo primitivo: ', type(algo))
print('tem espacos no que vc disse? ', algo.isspace())
print('eh um numero? ', algo.isnumeric())
print('eh alfabetico? ', algo.isalpha())
print('eh alfanumerico?', algo.isalnum())
print('esta em maiuscula? ', algo.isupper())
print('esta em minuscula? ', algo.islower())
print('esta capitalizada?', algo.istitle())