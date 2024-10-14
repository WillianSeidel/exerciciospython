#estrutura de repetição for e while

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

#função range é utilizado o iterador i
for numero in range(0, 11):
    print(numero, end="")
#terceiro item acrescenta o numero que ele deve percorrer
for numero in range(0, 51, 5):
    print(numero, end="")
print()

#usando a repetição while exemplo
opcao = -1
while opcao != 0:
    opcao = int(input("[1] sacar [2] extrato [0] sair")) 
    if opcao == 1:
        print("sacando")
    elif opcao ==2:
        print("ex docs")
else:
    print("valeu pela pa")