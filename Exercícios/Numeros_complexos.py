import math

class Complexo:
    '''Representação de um número complexo'''

    def __init__(self, real, img):
        '''Inicialização da parte real e imaginária'''
        self.real = real
        self.img = img
    
    def reset(self):
        '''Reseta o numero complexo'''
        self.real = 0
        self.img = 0

    def incrementar(self):
        '''Soma +1 na parte real'''
        self.real +=1
    
    def modulo(self):
        '''Executa o modulo do numero complexo'''
        return math.sqrt( math.pow(self.real, 2) + math.pow(self.img, 2) )

    def conjugado(self):
        '''Conjuga o número complexo'''
        return Complexo(self.real, self.img * -1)

    def __str__(self):
        '''Representação em string de um numero complexo'''
        return f'{self.real} + {self.img}i'

    def soma(self, outro):
        '''Soma dois numeros complexos'''
        return Complexo(self.real + outro.real, self.img + outro.img)

    def __add__(self, outro):
        '''Implementa o operador +'''
        return self.soma(outro)

c1 = Complexo(2, 2)
c2 = Complexo(3, 6)
c3 = c1.soma(c2)
print(c3)
