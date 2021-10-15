from conta import Conta


class Contas:
    dic_contas = {}

    def cria_conta(self, num, cliente):
        conta = Conta(num, cliente, 0.0, 100.0)
        if not (self.dic_contas.get(conta.cliente.cpf)):
            self.dic_contas[conta.cliente.cpf] = conta
            return True
        else:
            return False

    def login(self, CPF, SENHA):
        if CPF in self.dic_contas.keys():
            if SENHA == self.dic_contas[CPF].cliente.senha:
                return True
            else:
                return False
        else:
            return False
