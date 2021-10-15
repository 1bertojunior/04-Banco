from registro import Contas
from cliente import Cliente


def operacao(op):
    if op:
        print('Operação realizada com sucesso.')
    else:
        print('Operação invalida!')


c1 = Cliente('João', 'Silva', '111', 'sopademacaco')
c2 = Cliente('Juliana', 'Sousa', '222', 'sopademacaco2')


conta = Contas()

operacao(conta.cria_conta('1234-5', c1))
operacao(conta.cria_conta('9876-5', c2))
a = conta.login('222', 'sopademacaco2')
b = conta.login('111', 'sopademacaco')
operacao(a)
operacao(b)
print(len(conta.dic_contas))
#print(conta.dic_contas['111'].numero)

# conta1 = Conta('123-4', c1, 120.0, 1000.0)
# conta2 = Conta('678-9', c2, 123.4, 4000.0)
#
# operacao(conta1.deposita(100.0))
# operacao(conta1.saca(50.0))
#
# operacao(conta1.transferir(conta2, 20.0))
# operacao(conta2.transferir(conta1, 143.9))
#
# conta1.extrato()
# print('\n')
# conta1.historico.imprimir()
# conta2.historico.imprimir()
