


def saque(saldo):
    valor = saldo
    valor_digitado = float(input("Digite aqui o valor que você deseja sacar: "))
    valor -= valor_digitado
    return valor

def deposito(saldo):
    valor = saldo
    valor_digitado = float(input("Digite aqui o valor que você deseja depositar: "))
    valor += valor_digitado
    return valor