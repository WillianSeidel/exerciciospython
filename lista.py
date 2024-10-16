numeros = [10, 20, 30, 40, 50, 60, 70]

#somar a lista e media preciso dividir pelo numero da lista

soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(f"Media de {media}")