#vamos utiliazar o laço for com os metodos.abs

matricula = {
    'NºMatricula' : 2000168933,
    'DiaDeCadastro': 25,
    'MêsDeCadastro': 10,
    'Turma': "2E"}

for chaves in matricula.keys():
    print (matricula[chaves])

#neste caso não será mostrado as chaves e sim os valores delas