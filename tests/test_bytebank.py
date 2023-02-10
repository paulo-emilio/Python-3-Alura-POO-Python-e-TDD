from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23
        funionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funionario_teste.idade()  # When-Ação
        assert resultado == esperado  # Then-Desfecho]

    def test_quando_sobrenome_recebe_Darth_Loki_deve_retornar_Loki(self):
        entrada = '  Darth   Loki  '  # Given
        esperado = 'Loki'
        funcionario_teste = Funcionario(entrada, '08/08/1888', 8888)
        resultado = funcionario_teste.sobrenome()  # When
        assert resultado == esperado  # Then
