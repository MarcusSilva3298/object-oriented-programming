# Solução aos exercícios

def temRepetidos(l):
    '''Determina se l tem elementos repetidos'''
    return len(l) != len(set(l))

def estaOrdenada(l):
    '''Determina se l está ordenada'''
    l2 = l.copy()
    l2.sort()
    return l2 == l

def identidade(n):
    '''Retorna a matriz identidade n x n'''
    l = [None] * n
    
    for i in range(n):
        li = [0] * n
        l[i] = li
        li[i] = 1
    
        
    return l

CEP = {'59115-260': 'Rua Abdon Trigueiro',
       '59114-220':'Rua Abmael Florêncio Bernardo',
       '59072-645':'Avenida Abreu e Lima',
       '59080-520':'Rua Aeroporto de Congonhas',
       '59020-105':'Travessa Afonso Pena',
       '59090-200':'Rua Afonso Magalhães'
      }

def consultaCEP(cep):
    if cep in CEP:
        return CEP[cep]
    else:
        return 'CEP não cadastrado'

def listaContida(l1,l2):
    '''Determina se todos os elementos de l1 estão contidos em l2'''
    return set(l1) <= set(l2)

def ordemReversa(l):
    '''Retorna l em ordem reversa'''
    l2 = l.copy()
    l2.sort(reverse=True)
    return l2

print(temRepetidos([1,2,3]))
print(temRepetidos([1,2,3,1]))
print(estaOrdenada([1,2,3]))
print(estaOrdenada([1,6,3]))
print(identidade(3))
print(consultaCEP('59020-105'))
print(listaContida([6,1],[1,5,2,6]))
print(listaContida([6,8],[1,5,2,6]))
print(ordemReversa([1,5,2,6]))