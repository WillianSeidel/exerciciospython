# são utilizados para executar operações
# adição +
print(1 + 1)
# subtração -
print(2 - 1)
# multiplicação *
print(2 * 2)
# divisão retorna float
print(12 / 3)
# divisão inteira retorna inteiro
print(12 // 3)
# modulo da divisao
print(10 % 3)
#exponenciação
print(2 ** 3)
#operadores de comparação a é igual b
saldo = 400
saque = 200
#usando para verificar a igualdade ==
print(saldo == saque)
#usado para verificar a diferença
print(saldo != saque)
#usado para verificar maior
print(saldo > saque)
#usado para verificar maior igual
print(saldo >= saque)
#usado para verificar menor
print(saldo < saque)
#usado para verificar menor igual
print(saldo <= saque)
#operadores de atribuição usado para atribuir o valor
#atribuição simples ponto é variavel valores são valores
ponto = 10
ponto += 100 
print(str(ponto))
#operadores logicos são utilizados para construir uma expressão
compra = 200
venda = 1000
limite = 100
compra >= saque and venda <= limite
# verdadeira e falso portanto falso
compra >= saque or venda <= limite
#verdadeiro ou salso prontanto verdade
not 1000 > 1500
# operador not é a negação portanto o print saira verdadeiro
#operadores de identidade
# is e is not
curso = "curso python"
nome_curso = curso
saldo, limite = 200, 200
curso is nome_curso # true
curso is not nome_curso # false
saldo is limite #true
#operadores de associação
#verificar se objeto esta em uma squencia 
curso = "curso python"
frutas = ["laranja", "uva", "limao"]
saques = [1500, 100]

"python" in curso #true
"maça" not in frutas #true
200 in saques #false
print("laranga" in frutas)
print("py" in curso)