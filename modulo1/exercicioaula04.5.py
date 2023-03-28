print("Atividade de sala - Messias | Questão 5")
n_conta = float(input("Digite o número da sua conta: "))
saldo = float(input("Digite o seu saldo: "))
debito = float(input("Digite o seu débito: "))
credito = float(input("Digite o seu crédito: "))
saldo_atual = saldo - debito + credito
if saldo_atual >= 0:
    print (f"Seu saldo é positivo, R${saldo_atual}")
else:
    print (f"Seu saldo é negativo, R${saldo_atual}")