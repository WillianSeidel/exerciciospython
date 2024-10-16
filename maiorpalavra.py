palavras = ["python", "asimov", "código", "web", "programação"]

#vou precisar percorrer a lista e armazenar a maior e menor palavra e contar os caracteres de cada string e depois realizar impressao da maior palavra

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print("Maior palavra", maior_palavra) 
print("e a menor palavra", menor_palavra)

frutas = ["uva", "maça", "abacate", "banana"]

#vou precisar armazenar a maior palavra e a menor depois percorrer a lista e susbstituit caso encontre
fruta_maior = frutas[0]
fruta_menor = frutas[0]

for fruta in frutas:
    if len(fruta) > len(fruta_maior):
        fruta_maior = fruta
    if len(fruta) < len(fruta_menor):
        fruta_menor = fruta   
print(fruta_maior)
print(fruta_menor) 

carros = ["uno", "pali", "unoooooooooo", "kombiiii"]

#primeiro preciso armazenar o maior e o menor e depois percorrer a lista caso encontre maior realiza uma nova atribuição

carro_maior = carros[0]
carro_menor = carros[0]

for carro in carros:
    if len(carro) > len(carro_maior):
        carro_maior = carro
    if len(carro) < len(carro_menor):
        carro_menor = carro
print(carro_maior)
print(carro_menor)

nomes = ["udo", "bianca", "julia", "roberto"]

#primeiro preciso armazenar o valor em algum lugar, depois preciso percorrer a lista e depois substituir o valor se for maior ou menor

nome_maior = nomes[0]
nome_menor = nomes[0]

for nome in nomes:
    if len (nome) > len(nome_maior):
        nome_maior = nome
    if len(nome) < len(nome_menor):
        nome_menor = nome


print(nome_maior)
print(nome_menor)