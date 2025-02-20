#o pop() exclui uma chave valor de um dicionario

matricula = {
    'NºMatricula' : 2000168933,
    'DiaDeCadastro': 25,
    'MêsDeCadastro': 10,
    'Turma': "2E"}

matricula.pop('Turma')
print(matricula)