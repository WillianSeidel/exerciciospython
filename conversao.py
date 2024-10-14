#conversão de tipos string para int etc...

#inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

#float para inteiro
preco = float(10.30)
print(preco)

preco = int(preco)
print(preco)

#numero para string
s_preco = 5.0
print(str(preco))

texto = f'O preço é {preco} mas converti em string {s_preco} valeu'
print(texto)

#string para numero
preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

IDADE = bool(idade)
#bool verdade
#não consegue converter streing para float quando não existir numero
#perguntar o tipo type
print(type(IDADE))

#// retorna sempre o inteiro