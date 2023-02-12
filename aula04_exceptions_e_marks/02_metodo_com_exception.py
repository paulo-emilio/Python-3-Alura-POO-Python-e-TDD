from codigo.bytebank import Funcionario

ana = Funcionario('Ana', '12/03/1997', 100000)

print(ana.calcular_bonus())


# Teste criado em test_bytebank:
'''
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '10/10/1910', entrada)
        resultado = funcionario_teste.calcular_bonus()  # when
        
        assert esperado == resultado  # then
'''

# Sobre erros no Python, existem 2 tipos:
# SyntaxError: erro na própria linguagem, ex: 'parênteses )' a mais ou menos
# Exception: erro de excessão, ex: tentar dividir 0 por 0, ocorre o erro 'ZeroDivisionError, ou seja, personalizado

# criei um raise no método calcular_bonus:
'''raise Exception('O salário é muito alto para receber um bônus')'''


