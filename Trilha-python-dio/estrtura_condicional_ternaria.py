saldo = float(input("Qual seu saldo? "))
saque = float(input("qual é seu saque? "))

# tudo que esta em primeiro vai retornar se for verdaedira a primeira condições, se der falso
#retorna a segunda condições,
status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque, seu saldo ficou {saldo - saque}")