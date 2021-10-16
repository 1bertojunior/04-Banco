from Classes.Conta import Conta


class Banco:
    dic_contas = {}

    def getClientePorCpf(self, cpf) -> bool:
        if cpf in self.dic_contas.keys():
            return True
        else:
            return False
    
    def checkNumDaConta(self, num) -> bool:
        for i in self.dic_contas.keys():
            if self.dic_contas[i].numero == num:
                return True
        return False
            
    def cria_conta(self, num, cliente):
        conta = Conta(num, cliente, 100.0, 100.0)
        if not (self.dic_contas.get(conta.cliente.cpf)):
            self.dic_contas[conta.cliente.cpf] = conta
            return True
        else:
            return False

    def login(self, CPF, SENHA):
        if CPF in self.dic_contas.keys():
            print("{} == {} ".format(SENHA, self.dic_contas[CPF].cliente.senha))
            if SENHA == self.dic_contas[CPF].cliente.senha:
                return True
            else:
                return False
        else:
            return False
