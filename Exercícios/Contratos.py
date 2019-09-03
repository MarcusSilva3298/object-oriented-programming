import datetime

class Profissional:

    def __init__(self, nome, exp, endereço, data, habilidades=[]):
        self._nome = nome
        self._habilidades = habilidades
        self._profissoes = []
        self._exp = exp
        self._endereço = endereço
        self._ddn = data
    
    def __str__(self):
        #Habilidades
        s = 'Habilidades:{\n'
        for i in self._habilidades:
            s+=f'\t{i};\n'
        s +='}'

        #Profissões
        p = 'Profissões:{\n'
        for i in self._profissoes:
            p+=f'\t{i}\n'
        p +='}'

        #Return
        return f'Nome do Profissional: {self._nome}; Anos de experiência: {self._exp}; Enderço: {self._endereço}; Data de nascimento: {self._ddn}; \n{s};\n{p}'

    def addHabilidade(self, habilidade):
        '''
        Adiciona uma nova habilidade ao profissional
        '''
        self._habilidades.append(habilidade)

    def removeHabilidade(self, habilidade):
        '''
        Remove uma habilidade do profissional
        '''
        self._habilidades.remove(habilidade)

    def trocarHabilidade(self, a_habilidade, n_habilidade):
        '''
        Substitui uma habilidade que o profissional já possui por uma nova (upgrade ou simples troca)
        '''
        self.removeHabilidade(a_habilidade)
        self.addHabilidade(n_habilidade)

    def addProfissão(self, profissao):
        '''
        Adiciona uma profissão ao profissional caso esse possua as habilidades necessárias
        '''
        for i in profissao._habi_nece:
            ok = True
            cont = 0
            for j in self._habilidades: 
                if i == j: 
                    cont +=1
                    break
            if cont is 0:
                ok = False
                break
        
        if ok == True:
            self._profissoes.append(profissao._nome)
            print(f'{self._nome} foi cadastrado na profissão: {profissao._nome}')
        else:
            print(f'{self._nome} não possui as habilidades necessárias')

    def candidatarOferta(self, oferta):
        '''
        Candidata o profissional a oferta, caso ele possua a profissão necessária
        '''
        ok = False
        for i in self._profissoes:
            if i == oferta._prof:
                ok = True
        if ok is False:
            print(f'O candidato {self._nome} não possui a profissão necessária')
        if ok is True:
            oferta._candidatos.append(self)
            print(f'Candidato {self._nome} cadastrado')

    def melhor(self, outro):
        '''
        Define entre dois profissionais qual é o melhor baseado no tempo de experiência em anos
        '''
        if self._exp > outro._exp:
            return self
        elif self._exp < outro._exp:
            return outro
        else:
            return self and outro

class Profissão:

    def __init__(self, nome, habi_nece=[]):
        self._nome = nome
        self._habi_nece = habi_nece

    def __str__(self):
        h = 'Habilidades Necessárias:{\n'
        for i in self._habi_nece:
            h += f'\t{i}\n'
        h += '}'
        
        return f'Nome da Profissão: {self._nome}; {h}'

    def __eq__(self, outro):
        return self._nome == outro._nome
    
class Empresa:

    def __init__(self, nome, cnpj, endereço):
        self._nome = nome
        self._oferta = []
        self._cnpj = cnpj
        self._endereço = endereço

    def __str__(self):
        #Ofertas da Empresa
        o = '{\n'
        for i in self._oferta:
            o += f'\t{i._prof}; Salário: {i._salario};\n'
        o +='}'

        #Return
        return f'Nome da Empresa: {self._nome};\nProfissões ofertadas pela empresa no momento:{o}'

    def addOferta(self, oferta):
        '''
        Adiciona uma oferta ao 'catálogo' de ofertas de emprego da empresa
        '''
        print(f'Oferta de {oferta._prof} lançada')
        self._oferta.append(oferta)


class Oferta:

    def __init__(self, nid, prof, salario):
        self._id = nid
        self._prof = prof
        self._salario = salario
        self._candidatos = []

    def melhor(self):
        '''
        Define qual o melhor candaditato a oferta, baseado em seus anos de experiência
        '''
        melhor = self._candidatos[1]
        for i in self._candidatos:
            m = melhor.melhor(i)
            if m is not melhor:
                melhor = m

        return melhor._nome

    def __str__(self):
        #Candidatos
        c = '{\n'
        for i in self._candidatos:
            c += f'\t{i._nome}\n'
        if len(self._candidatos) is not 0:
            c += f'\n\tMelhor candidato: {self.melhor()}\n'
        c += '}'

        #Return
        return f'Profissão ofertada: {self._prof}; Salário: {self._salario}; Offer ID:{self._id}; Candidatos à oferta no momento: {c};'


print('------------------------------------ Test Area ------------------------------------\n')





print('\n-----------------------------------------------------------------------------------')
