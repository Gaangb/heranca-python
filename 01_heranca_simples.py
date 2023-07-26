# Neste código faço praticas de POO usando a lingaguem python. 
# Estou criando uma classe Veiculo, Motocicleta, Carro e Caminhao, sendo que as ultimas 3 herdam de Veiculo
# Adicionei em Caminhao opcao de carga, descarga e verificar carga


class Veiculo:
    def __init__(self, cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

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
            print("Carga adicionada")

    def descarregar(self):
        if self.carregado:
            self.carregado = False
            print("Carga retirada")
        else:
            print("Caminhão não possui carga")
    



moto = Motocicleta("vermelha", "PJK-3322", 2)
moto.ligar_motor()

carro = Carro("branco", "xdd-d3e", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "JKJ-2211", 8)
caminhao.verificar_carga()
caminhao.adicionar_carga()
caminhao.verificar_carga()

print(caminhao)
print(moto)
print(carro)