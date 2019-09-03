class Carro:

    def __init__(self, placa):
        self._placa = placa

    @property
    def placa(self):
        return self._placa
    
    def __str__(self):
        return f'Carro da placa: {self._placa}'

class Andar:

    def __init__(self, capacidade):
        self._vagas = [None]*capacidade
        self._capac = capacidade

    def __str__(self):
        return f'Capacidade Máxima: {self._capac}\nVagas disponíveis: {self.vagas()}'

    def entrar(self, posição, carro):
        if self._vagas[posição] is None:
            self._vagas[posição] = carro
        else:
            print('Vaga ocupada')

    def sair(self, posição):
        if self._vagas[posição] is None:
            print('Vaga livre')
        else:
            self._vagas[posição] = None

    def vagas(self):
        self.vdp = self._vagas.count(None)
        return self.vdp

    def carros(self):
        return self._capac - self.vdp

    def temVagas(self):
        if self.vdp > 0:
            return True
        else:
            return False

    def temCarros(self):
        if self.vdp is self._capac:
            return False
        else:
            return True


class Estacionamento:

    def __init__(self, andar):
        self._andares = andar

    def __str__(self):
        return f'Pavimento: {self._andares[0].vagas()} vagas \n1º andar: {self._andares[1].vagas()} vagas\n2º andar {self._andares[2].vagas()} vagas'

    def entrar(self, andar, posição, carro):
        if self._andares[andar]._vagas[posição] is None:
            self._andares[andar]._vagas[posição] = carro
        else:
            print('Vaga do andar indisponível')

    def sair(self, andar, posição):
        if self._andares[andar]._vagas[posição] is not None:
            print('Vaga do andar Livre')
        else:
            self._andares[andar]._vagas[posição] = None


print("-------------------------------------------------------\n")

c1 = Carro(1234)
c2 = Carro(3214)
c3 = Carro(5320)
print(c1)
print(c2)
print(c3)

a1 = Andar(100)
a2 = Andar(100)
a3 = Andar(100)

e1 = Estacionamento([a1, a2, a3])
e1.entrar(1, 30, c2)
print(e1)
e1.entrar(1, 30, c1)
e1.entrar(0, 30, c1)
print(e1)
e1.sair(1, 29)
e1.sair(1, 30)
print(e1)
e1.entrar(2, 40, c2)
e1.entrar(0, 20, c1)
print(e1)
e1.sair(2, 40)
e1.sair(0, 20)
print(e1)
'''
print(a1.vagas())
a1.entrar(30, c1)
print(a1.vagas())
a1.sair(30)
print(a1.vagas())
'''

print("\n-------------------------------------------------------")