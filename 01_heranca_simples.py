# class Veiculo:
#     def __init__(self, cor, placa, numero_rodas):
#         self.cor = cor
#         self.placa = placa
#         self.numero_rodas = numero_rodas

#     def ligar_motor(self):
#         print("Ligando o motor")

#     def __str__(self):
#         return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# class Motocicleta(Veiculo):
#     pass


# class Carro(Veiculo):
#     pass


# class Caminhao(Veiculo):
#     def __init__(self, cor, placa, numero_rodas, carregado):
#         super().__init__(cor, placa, numero_rodas)
#         self.carregado = carregado

#     def esta_carregado(self):
#         print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# moto = Motocicleta("preta", "abc-1234", 2)
# carro = Carro("branco", "xde-0098", 4)
# caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# print(moto)
# print(carro)
# print(caminhao)


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

    def adicionar_carga(self, carregado):
        if carregado:
            print("Caminhão já esta carregado")
        else:
            carregado = True

    

    def __str__(self):
        return self.cor



moto = Motocicleta("vermelha", "PJK-3322", 2)
moto.ligar_motor()

carro = Carro("branco", "xdd-d3e", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "JKJ-2211", 8)
caminhao.verificar_carga()
caminhao.ligar_motor()