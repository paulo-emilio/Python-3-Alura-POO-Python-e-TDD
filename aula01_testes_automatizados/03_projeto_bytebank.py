from codigo.bytebank_original import Funcionario

# criando um ambiente virtual no windows:
# No terminal:
# python -m venv venv
# ativando:
# venv/Scripts/activate

# Testando o codigo.bytebank

paulo = Funcionario('Paulo Emílio', '10/05/2000', 1312)

print(paulo.idade())  # não roda pois o método idade so funciona se colocarmos só o ano de nascimento


