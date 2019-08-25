#Solução: exercício de Listas Encadeadas
class Celula:
    '''Armazena um objeto e a referência à próxima célula'''

    def __init__(self, value):
        self.next = None 
        self.value = value

    def __str__(self):
        return f'{self.value}'

class Lista:
    '''Implementação de uma lista simplesmente encadeada'''

    def __init__(self):
        self.__head = None #Primeiro elemento
        self.__tamanho = 0 #Tamanho da lista
        self.__tail = None #Ultimo elemento

    @property
    def tamanho(self):
        '''Get para __tamanho'''
        return self.__tamanho

    def adicionar(self, value):
        '''Adicionar value no final lista'''
        #Criamos uma célula
        C = Celula(value)

        if self.__head is None:
            self.__head = C
            self.__tail = C
        else:
            self.__tail.next = C
            self.__tail = C

        self.__tamanho += 1

    def inserir(self, value):
        '''Inserir value no inicio da lista'''
        C = Celula(value)
        C.next = self.__head

        #Caso lista vazia
        if self.__tail is None:
            self.__tail = C

        self.__head = C
        self.__tamanho += 1

    def adicionarPos(self, pos, value):
        '''Adicionar value antes da posição pos'''
        if pos<0 or pos >= self.__tamanho:
            print(f'{pos} fora dos limites')
            return

        if pos ==0:
            #se pos=0, devemos atualizar também self.__head. O método inserir toma conta disso
            self.inserir(value)
        else:
            C = Celula(value)
            # l é uma referência à célula antes de pos
            l = self.__head
            for i in range(pos-1):
                l = l.next

            C.next = l.next
            l.next = C
            
            self.__tamanho += 1

    def elemento(self, pos):
        '''Retorna o elemento em pos'''
        if pos<0 or pos >= self.__tamanho:
            print(f'{pos} fora dos limites')
            return None
        l = self.__head
        for i in range(pos):
            l = l.next

        return l.value


    def __str__(self):
        s = "[ "
        l = self.__head
        while l is not None:
            if l != self.__head:
                s += " -> "
            s+= f'({l})'
            l = l.next

        return s + " ]"

L = Lista()
print(L)
L.adicionar(1)
print(L.tamanho)
L.adicionar(2)
print(L)
print(L.elemento(1))
L2 = Lista()
for i in range(10):
    L2.adicionar(i)
print(L2)
for i in range(10):
    L2.inserir(-1 * i)
print(L2)

print('=============')
L3 = Lista()
L3.adicionar('d')
print(L3)
L3.adicionarPos(0,'a')
print(L3)
L3.adicionarPos(1,'b')
print(L3)
L3.adicionarPos(2,'c')
print(L3)