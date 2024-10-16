#Realize a impressao do impar par do ususario com o numero informado

numero = int(input())

if numero % 2 == 0:
    print(f"Este numero {numero} é par")
else:
    print(f"Este numero {numero} é impar")

#realize permissao de dirigir 18 anos mais se for menor proibido

CNH = 18

idade = int(input("Insira sua idade"))

if idade >= CNH:
    print("Voce pode dirigir")
if idade < CNH: 
    print("voce não pode dirigir")

# apresenten-se com idade, nome e profissão

nome = str(input("Insira seu nome"))
idade = int(input("coloque sua idade"))
profissao = str(input("sua profissao"))

apresentacao = str(f"Meu nome é {nome}, tenho {idade} de idade e profissao é {profissao}")

print(apresentacao)

#calcule a média
numeros = [10, 20, 30, 40, 50]
#armaznear a soma total em uma variavel, criar a media depois dividir pelo numeros da lista e apresentar a media

soma = sum(numeros)
media = soma / len(numeros) 

print(media)

soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)
print(media)

#calcule que gastou mais
gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

#preciso armazenar o gasto de cada um em uma variavel e depois comparar e imprimir

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print("joao gastou")
elif total_pedro > total_joao:
    print("pedro gastou")
