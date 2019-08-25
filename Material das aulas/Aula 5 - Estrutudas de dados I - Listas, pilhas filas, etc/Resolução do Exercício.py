#Solução exercício Listas

class Lista:
    '''Lista de produtos utilizando arranjos'''
    def __init__(self, TAM=5):
        self.TAM = TAM
        #Elementos da lista 
        # Inicialmente: [None, None, None ,... None]
        self.__elems = [None]*TAM
        #Último índice
        self.__ultimo = 0

    def adicionar(self, P):    
        ''' Inserir um produto no final da lista.'''

        tamanho = len(self.__elems)
        if self.__ultimo >= tamanho:
            #Lista sem espaço
            print("A lista precisa de mais espaco")
            # Criar um novo array
            elems = [None] * (tamanho + self.TAM)
            # Copiar os elements
            self.__copiar(elems)
            # o novo array é elems
            self.__elems = elems

        #Inserir o elemento
        self.__elems[self.__ultimo] = P
        self.__ultimo+= 1


    def __copiar(self, elems):
        '''Metodo auxiliar para copiar os produtos'''
        #Existe uma forma mais "Pythonic" de fazer isto... com enumerate
        for i in range(len(self.__elems)):
            elems[i] = self.__elems[i]

    def tamanho(self):
        ''' Retorna o numero de elementos na lista'''
        return self.__ultimo

    def elemento(self, pos=0):
        '''Retorna o elemento na posição pos'''
        if pos < 0 or pos >= self.__ultimo:
            print("Posição não válida");
            return None
        else:
            return self.__elems[pos];

    def __str__(self):
        s = "[";
        i=0
        while i<self.__ultimo:
            if i != 0: s += " , "
            s += str(self.__elems[i])
            i += 1

        s += " ] "
        return s

    def vazia(self):
        '''Deterermina se L está vazia'''
        return self.__ultimo == 0

    def buscar(self, e):
        ''' Buscar e na lista'''
        for i in range(self.__ultimo):
            if self.__elems[i] == e: return True
        
        return False


    def remover(self,pos):
        '''Remover o elemento na posição pos'''
        if pos <0 or pos >= self.__ultimo:
            print("Posição não válida")
            return

        #Deslocar os elementos
        for i in range(pos, self.__ultimo -1 ):
            self.__elems[i] = self.__elems[i+1]
            

        self.__ultimo -= 1
        self.__elems[self.__ultimo]=None

    def reset(self):
        '''Remover todos os elementos'''
        for i in range(self.__ultimo):
            self.__elems[i] = None
        self.__ultimo = 0

    def copiar(self):
        '''Criar uma copia da lista'''
        L = Lista()
        for i in range(self.__ultimo):
            L.adicionar(self.__elems[i])

        return L

    def __add__(self, L):
        '''Concatenar'''
        L2 = self.copiar()
        for i in range(L.__ultimo):
            L2.adicionar(L.__elems[i])
        return L2

    def reverso(self):
        '''Reverso da lista'''
        L = self.copiar()
        for i  in  range(L.__ultimo // 2):
            v = L.__elems[i]
            L.__elems[i] = L.__elems[L.__ultimo - i - 1]
            L.__elems[L.__ultimo - i - 1] = v
        return L


L1 = Lista()
L2 = Lista()
for i in range(10):
    L1.adicionar(i)
    L2.adicionar(i*2)

print(L1)
L1a = L1.reverso()
print(L1a)
print(L2)
L3 = L1 + L2
print(L3)
L3.remover(6)
print(L3)
L3.remover(18)
print(L3)
L4 = Lista()
L4.adicionar(5)
L4.remover(0)
print(L4)

