# oriatação a objetos = classes e objetos
# classes = bicicleta
# objetos = 
class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plin, Plin")

    def parar(self):
        print("bicicleta parada")

    def correr(self):
        print("bicicleta andando")


B1 = bicicleta("Branca", "esporte", 2024, 600)
B1.buzinar()
B1.correr()
B1.parar()

print(B1.cor, B1.valor)


B2 = bicicleta("verde", "mornark", 2000, 189)
bicicleta.buzinar(B2)

class cachorro:
    def __init__(self, nome, cor, acordado):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    #metodo destrutor __del__ =  serve para deletar e liberar memoria 
    
