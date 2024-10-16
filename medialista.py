numeros = [1,2,3,4,5,6,7,8,9]

#preciso somar e depois para a media dividir pela lista

soma = 0

for numero in numeros:
    soma += numero
print(soma)
media = soma / len(numeros)

print(f"A média é de {int(media)}")