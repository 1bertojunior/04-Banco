from Classes.Banco import *
from Classes.Cliente import Cliente
import socket

banco = Banco()

def conectView(view):
    if view[0] == 'Deposit':
        valor = view[1]
        msg = ''
        if banco.depositar(banco.idClient, float(valor)):
            msg = 'True'
        else:
            msg = 'False'
        con.send(msg.encode())

    elif view[0] == 'Historic':
        list_historic = list(banco.historico.getHistorico())
        msg = ""
        for i in list_historic:
            msg += str(i) + "\n"
        con.send(msg.encode())

    elif view[0] == 'Login':
        # cpf = con.recv(1024).decode()
        # password = con.recv(1024).decode()
        print(f'Entrou no login\nCPF: {view[1]}\nSENHA: {view[2]}')
        if view[1] != '' and view[2] != '':
            if banco.login(view[1], view[2]):
                msg = "True"
            else:
                msg = "False"
            con.send(msg.encode())

    elif view[0] == 'Register':
        # cpf = con.recv(1024).decode()
        msg = ''
        if banco.getClientePorCpf(view[3]):
            msg = 'True'
            #con.send(msg.encode())
        else:
            msg = 'False'
            #con.send(msg.encode())
            # account = con.recv(1024).decode()
            if banco.checkNumDaConta(view[4]):
                msg = 'False,True'
                #con.send(msg.encode())
            else:
                msg = 'False,False,False'
                # con.send(msg.encode())
                # name = con.recv(1024).decode()
                # surname = con.recv(1024).decode()
                # password = con.recv(1024).decode()
                c = Cliente(view[1], view[2], view[3], view[5])
                banco.cria_conta(view[4], c)
        con.send(msg.encode())

    elif view[0] == 'Transfer':
        cpf = view[1]
        value = float(view[2])
        balance = banco.getBalanceAccount(cpf)
        # con.send(str(balance).encode())
        msg = ''
        if value > 0 and value <= balance:
            conta = view[3]
            if banco.checkNumDaConta(conta):
                msg = f'True, , ,{balance}'
                # con.send(msg.encode())
                if banco.saca(banco.idClient, value, 1, conta):
                    msg = f'True,True, ,{balance}'
                    # con.send(msg.encode())
                    if banco.depositar2(conta, value):
                        msg = f'True,True,True,{balance}'
                        # con.send(msg.encode())
                    else:
                        msg = f'True,True,False,{balance}'
                        # con.send(msg.encode())
                else:
                    msg = f'True,False, ,{balance}'
                    # con.send(msg.encode())
            else:
                msg = f'False, , ,{balance}'
        else:
            msg = f'False, , ,{balance}'
        con.send(msg.encode())

    elif view[0] == 'Withdraw':
        cpf = view[1]
        balance = banco.getBalanceAccount(cpf)
        # con.send(str(balance).encode())
        valor = view[2]
        msg = ''
        if float(valor) > 0 and float(valor) <= balance:
            banco.saca(banco.idClient, float(valor))
            msg = f'True,{balance}'
        else:
            msg = f'False,{balance}'
        con.send(msg.encode())

    elif view[0] == 'Balance':
        cpf = view[1]
        balance = banco.getBalanceAccount(cpf)
        con.send(str(balance).encode())



# banco = Banco()
host = 'localhost'
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
op = 1

while op:
    print('aguardando conexao...')
    con, cliente = serv_socket.accept()
    print('conectado')
    print('aguardando mensagem...')
    view = ''
    str_list = ['']

    while str_list[0] != 'SAIR':
        view = con.recv(1024).decode()
        str_list = view.split(',')
        print(str_list[0])
        # conectView(view)
        if str_list[0] != 'SAIR':
            conectView(str_list)

    # print('\n[!] - Conexão com o cliente encerrada')
    # op = int(input('\t[1] - Continuar\n\t[0] - Encerrar\nOP: '))

serv_socket.close()
