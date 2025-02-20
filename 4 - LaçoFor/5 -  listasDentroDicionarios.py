# podemos relacionar listas dentro de dicionarios
#com isso iremos poder atribuir muitos valores a uma chave-valor transformando-a em uma lista

carros = { 'modelo': ['civic', 'palio', 'fit', 'corolla', 'onix'],
            'ano' : [2008, 2004, 2016, 2010, 2018]}

for chave, elementos in carros.items():
    print  (f'chave {chave} \nelementos')
    for dado in elementos:
        print (dado)
#usando o laço for para exibir o dicionario