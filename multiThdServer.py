import socket
import threading

from PyQt5.QtCore import reset

from Classes.Banco import *
from Classes.Cliente import Cliente
import socket

banco = Banco()


class ClientThread(threading.Thread):
    def __init__(self, clientAdress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print('Nova conexão', clientAdress)

    def run(self):
        print('Conectado de ', clientAdress)
        msg = ''
        self.view = ['']


        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            # self.csocket.send(msg.encode())
        
            self.view = msg.split(',')

            print(self.view [0])
            # self.conectView()
            print('From client: ', msg)
            if msg == 'SAIR':
                break
            else:
                self.conectView()
            
        print('Client at', clientAdress, 'desconected')
    
    def conectView(self):
        sinc = threading.Lock()
        if self.view[0] == 'Deposit':
            valor = self.view[1]
            msg = ''

            sinc.acquire()
            result = banco.depositar(banco.idClient, float(valor))
            sinc.release()

            if result:
                msg = 'True'
            else:
                msg = 'False'
            self.csocket.send(msg.encode())
        
        elif self.view[0] == 'Withdraw':

            cpf = self.view[1]
            balance = banco.getBalanceAccount(cpf)
            # con.send(str(balance).encode())
            valor = self.view[2]
            msg = ''
            if float(valor) > 0 and float(valor) <= balance:
                sinc.acquire()
                banco.saca(banco.idClient, float(valor))
                sinc.release()
                msg = f'True,{balance}'
            else:
                msg = f'False,{balance}'
            self.csocket.send(msg.encode())

        elif self.view[0] == 'Balance':
            cpf = self.view[1]
            
            sinc.acquire()
            balance = banco.getBalanceAccount(cpf)
            sinc.release()

            self.csocket.send(str(balance).encode())

        elif self.view[0] == 'Historic':
            
            list_historic = list(banco.historico.getHistorico())
            msg = ""
            if list_historic != None:
                for i in list_historic:
                    msg += str(i) + "\n"
            self.csocket.send(msg.encode())

        elif self.view[0] == 'Login':
            # cpf = con.recv(1024).decode()
            # password = con.recv(1024).decode()
            print(f'Entrou no login\nCPF: {self.view[1]}\nSENHA: {self.view[2]}')
            print(self.view)
            if self.view[1] != '' and self.view[2] != '':
                result =  banco.login(self.view[1], self.view[2])
                print("# TESTE: ", result)
                if result:
                    msg = "True"
                else:
                    msg = "False"
                self.csocket.send(msg.encode())

        elif self.view[0] == 'Register':
            # cpf = con.recv(1024).decode()
            msg = ''
            if banco.getClientePorCpf(self.view[3]):
                msg = 'True'
                #con.send(msg.encode())
            else:
                msg = 'False'
                #con.send(msg.encode())
                # account = con.recv(1024).decode()
                if banco.checkNumDaConta(self.view[4]):
                    msg = 'False,True'
                    #con.send(msg.encode())
                else:
                    msg = 'False,False,False'
                    # con.send(msg.encode())
                    # name = con.recv(1024).decode()
                    # surname = con.recv(1024).decode()
                    # password = con.recv(1024).decode()
                    c = Cliente(self.view[1], self.view[2], self.view[3], self.view[5])
                    banco.cria_conta(self.view[4], c)
            self.csocket.send(msg.encode())

        elif self.view[0] == 'Transfer':
            cpf = self.view[1]
            value = float(self.view[2])
            balance = banco.getBalanceAccount(cpf)
            # con.send(str(balance).encode())
            msg = ''
            if value > 0 and value <= balance:
                conta = self.view[3]
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
            self.csocket.send(msg.encode())

        

if __name__ == '__main__':
    LOCALHOST = ''
    PORT = 7005
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print('Servidor Iniciado')
    print('aguardando conexao...')

    while True:
        server.listen(1)
        clientSocket, clientAdress = server.accept()
        newThread = ClientThread(clientAdress, clientSocket)
        newThread.start()

# ---------------------------------------------------------------
# host = 'localhost'
# port = 8000
# addr = (host, port)
# serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# serv_socket.bind(addr)
# serv_socket.listen(10)
# op = 1
#
# while op:
#     print('aguardando conexao...')
#     con, cliente = serv_socket.accept()
#     print('conectado')
#     print('aguardando mensagem...')
#     recebe = ''
#
#     while recebe.upper().strip() != 'SAIR':
#         recebe = con.recv(1024).decode()
#         if recebe.upper().strip() != 'SAIR':
#             print('mensagem recebida: ' + recebe)
#             enviar = input('digite uma mensagem para enviar ao cliente: ')
#             con.send(enviar.encode())
#
#     print('\n[!] - Conexão com o cliente encerrada')
#     op = int(input('\t[1] - Continuar\n\t[0] - Encerrar\nOP: '))
#
# serv_socket.close()
