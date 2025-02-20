#vamos mostrar tanto as chaves quanto os valores usando dois elementos com o for:


matricula = {
    'NºMatricula' : 2000168933,
    'DiaDeCadastro': 25,
    'MêsDeCadastro': 10,
    'Turma': "2E"}

for chaves, valores in matricula.items():
    print(chaves, valores)