#é a capacidade de uma classe filha derivar ou herdar as caracteristicas e comportamentos da classe pai

#herança simples é quando a classe filha herda apenas de uma classe base

#herança multipla é quando a classe filha herda de varias classes bases

class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    
    def ligar_motor(self):
        print("ligando motor")

class motocicleta(veiculo):
    def servico(self):
        print("Usado como taxi")

class carro(veiculo):
    pass
class caminhao(veiculo):
    pass

moto = motocicleta("preta", "MBZ9097", 2)
print(moto)
moto.ligar_motor