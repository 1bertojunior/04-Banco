class Cliente:
    total_clientes = 0
    __slots__ = ['_nome', '_sobrenome', '_cpf', '_senha']

    def __init__(self, nome, sobrenome, cpf, senha):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._senha = senha
        Cliente.total_clientes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, new_sob):
        self._sobrenome = new_sob

    @property
    def cpf(self):
        return self._cpf

    @property
    def senha(self):
        return self._senha

    @cpf.setter
    def cpf(self, new_cpf):
        self._cpf = new_cpf

    def imprimir_cliente(self):
        print(f'Nome: {self.nome} {self.sobrenome}\nCPF: {self.cpf}')
