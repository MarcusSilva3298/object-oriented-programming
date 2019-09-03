class Cafe:
    def __init__(self, prc):
        self.__prc = prc
        self.__saldo = prc
        self.__cfdp = True
    
    def __str__(self):
        return f'Preço do cafe: {self.__prc} centavos'

    def get_saldo(self, vp):
        if self.__saldo == 0: 
            print('Café disponível!')
        elif self.__saldo < 0:
            troco = vp + self.__saldo
            print(f'troco: {troco}')
            print('Café disponível')

    def inserirMoeda(self, vp):
        if vp!=10 and vp!=5:
            print('Esta maquina so aceita moedas de 5 ou 10 centavos')
        else:
            self.__saldo -= vp
            print(f'Moeda de {vp} centavos inserida; Faltam {self.__saldo} centavos')
            Cafe.get_saldo(self, vp)


#if antes do inserir moeda pra saldo>0
c = Cafe(10)
c.inserirMoeda(5)
c.inserirMoeda(10)
