#o Join(). é utilizado para transformar uma lista em string
# Para usar a função, precisamos definir o caractere unificador que será utilizado para unir os elementos da lista, Ex:

misturas = ['Tintas: vermelho, azul e amarelo',
            'Verde: mistura de azul e amarelo',
            'Laranja: mistura de vermelho e amarelo',
            'Roxo: mistura de vermelho e azul']
unificador = '. '
string_misturas = unificador.join(misturas)
print(string_misturas)