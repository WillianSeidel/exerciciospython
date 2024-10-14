

def sacar(valor):
    saldo = 500
    valor = 200
    if saldo >= valor:
        saldo -= valor

        print("Voce sacou 200 saldo de 300")
sacar(200)

#def depositar(valor):
    #saldo = 100
    #deposito += valor
    #if 200 + 100:
     #   print("saldo de 300")
#depositar(5)

#Estrutura condicional if if-esle elif servem para desviar o fluxo/controle
#if condicional simples
saldo = 1000.0
saque = float(input("informe o valor de saque:"))

if saldo >= saque:
    print("saque realizado")
if saldo < saque:
    print("saldo insuficiente")

#if e else
saldo = 1000.0
saque = float(input("informe o valor de saque:"))

if saldo >= saque:
    print("saque realizado")
else:
    print("saldo insuficiente")

#exemplo de uso elif

opcao = int(input("informe uma opção: [1] sacar ou [2] extrato"))

if opcao == 1:
    valor = float(input("informe o saque:"))
elif opcao == 2:
    print("exibindo extrato")
else:
    print("opção invalida")

