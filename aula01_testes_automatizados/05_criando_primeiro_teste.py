from codigo.bytebank import Funcionario

# na classe:
'''
def idade(self):
    data_nasc_quebrada = self._data_nascimento.split('/')
    ano_nasc = data_nasc_quebrada[-1]
    ano_atual = date.today().year
    return ano_atual - int(ano_nasc)
'''
'''
paulo = Funcionario('Paulo Emílio', '10/05/2000', 1312)
print(paulo.idade())  # funcionou
'''

# criando um teste automatizado:
def teste_idade():
    funcionario_teste = Funcionario('Teste', '06/06/1969', 15000)
    return print(f'Teste = {funcionario_teste.idade()}')

teste_idade()
