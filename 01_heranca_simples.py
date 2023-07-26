class Veiculo:
    def __init__(self, cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def verificar_carga(self):
        print(f"{'Caminhão com carga' if self.carregado else 'Caminhão sem carga'}")

    def adicionar_carga(self):
        if self.carregado:
            print("Caminhão já esta carregado")
        else:
            self.carregado = True

    def descarregar(self):
        if self.carregado:
            self.carregado = False
        else:
            print("Caminhão não possui carga")
    

    def __str__(self):
        return self.cor



moto = Motocicleta("vermelha", "PJK-3322", 2)
moto.ligar_motor()

carro = Carro("branco", "xdd-d3e", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "JKJ-2211", 8)
caminhao.verificar_carga()
caminhao.adicionar_carga()
caminhao.verificar_carga()
caminhao.ligar_motor()