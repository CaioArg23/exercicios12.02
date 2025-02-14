#mesmo assim é possível transformar uma string em uma lista através do método split(). Ex:
pergunta = "quem veio antes? O ovo? Ou a galinha?" #aqui temos uma string, na qual não é possivel alterar sua variável nem através de índices
listaFinal = pergunta.split('?') #transformando string em lista para cada "?" que aparece
print (listaFinal)