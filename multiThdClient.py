import socket

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication, reset, showbase
from PyQt5.sip import setdestroyonexit

import hashlib
import socket

from Views.Login import Login
from Views.Register import Register
from Views.Dashboard import Dashboard
from Views.Withdraw import Withdraw
from Views.Deposit import Deposit
from Views.Transfer import Transfer
from Views.Historic import Historic

def MD5hash(arg):
    result = ""
    if not (arg == ""):
        str = hashlib.md5()
        str.update(arg.encode('utf-8'))
        result = str.hexdigest()
    return result


def isEmpty(arg):
    return arg == ""


ip = 'localhost'
port = 7005
addr = (ip, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = ''

# while mensagem != 'SAIR':
#     # mensagem = input('digite uma mensagem para enviar ao servidor: ')
#     client_socket.send(mensagem.encode())
#     if mensagem.upper().strip() != 'SAIR':
#         print('mensagem enviada')
#         # msg_recebida = client_socket.recv(1024).decode()
#         # print('mensagem recebida: ' + msg_recebida)

# # client_socket.close()


# STYES
stylePopupErro = ("background-color: rgb(239, 41, 41); border-radius: 5px;")
stylePopupOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.screenLogin = Login()
        self.screenLogin.setupUi(self.stack0)

        self.screenRegistration = Register()
        self.screenRegistration.setupUi(self.stack1)

        self.screenDash = Dashboard()
        self.screenDash.setupUi(self.stack2)

        self.screenDeposit = Deposit()
        self.screenDeposit.setupUi(self.stack3)

        self.screenHistoric = Historic()
        self.screenHistoric.setupUi(self.stack4)

        self.screenTransfer = Transfer()
        self.screenTransfer.setupUi(self.stack5)

        self.screenWithdraw = Withdraw()
        self.screenWithdraw.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cpf = None

        # INIT
        # OCULTANDO POPUP DE MENSSAGEM
        self.hideFrameErro(self.screenLogin)
        self.hideFrameErro(self.screenRegistration)
        self.hideFrameErro(self.screenDash)
        self.hideFrameErro(self.screenWithdraw)
        self.hideFrameErro(self.screenDeposit)
        self.hideFrameErro(self.screenTransfer)
        self.hideFrameErro(self.screenHistoric)

        # BOT??ES
        # BTN FECHAR POPUP
        self.btnClosed(self.screenLogin)
        self.btnClosed(self.screenRegistration)
        self.btnClosed(self.screenDash)
        self.btnClosed(self.screenWithdraw)
        self.btnClosed(self.screenDeposit)
        self.btnClosed(self.screenTransfer)
        self.btnClosed(self.screenHistoric)

        # BTN VOLTAR
        self.screenRegistration.btn_back.clicked.connect(self.btnReturn)
        self.screenDash.btn_back.clicked.connect(self.btnReturn)
        self.screenWithdraw.btn_back.clicked.connect(lambda: self.openScreen(2))
        self.screenDeposit.btn_back.clicked.connect(lambda: self.openScreen(2))
        self.screenHistoric.btn_back.clicked.connect(lambda: self.openScreen(2))
        self.screenTransfer.btn_back.clicked.connect(lambda: self.openScreen(2))

        # LOGIN
        self.screenLogin.btn_login.clicked.connect(self.btnLogin)
        self.screenLogin.btn_register.clicked.connect(lambda: self.openScreen(1))

        # CADASTRO
        self.screenRegistration.btn_registration.clicked.connect(self.btnRegistration)

        # DASH
        self.screenDash.btn_withdraw.clicked.connect(lambda: self.openScreen(6))
        self.screenDash.btn.clicked.connect(lambda: self.openScreen(3))
        self.screenDash.btn_transfer.clicked.connect(lambda: self.openScreen(5))
        self.screenDash.btn_historic.clicked.connect(self.initHistoric)

        # SACAR
        self.screenWithdraw.btn_withdraw.clicked.connect(self.btnWithdraw)

        # DEPOSITAR
        self.screenDeposit.btn_deposit.clicked.connect(self.btnDeposit)

        # TRANSFERIR
        self.screenTransfer.btn_transfer.clicked.connect(self.btnTransfer)

    def btnWithdraw(self):
        value = self.screenWithdraw.in_value.value()
        mensagem = f'Withdraw,{self.cpf},{value}'
        client_socket.send(mensagem.encode())
        # mensagem = self.cpf
        # client_socket.send(mensagem.encode())
        msg_recebida = client_socket.recv(1024).decode()
        msg_recebida = msg_recebida.split(',')
        balance = float(msg_recebida[1])
        # balance = banco.getBalanceAccount(self.cpf)

        # mensagem = str(value)
        # client_socket.send(mensagem.encode())

        if msg_recebida[0] == 'True':
            # query = "UPDATE account SET balance = balance - %s WHERE fk_client = %s"
            # banco.db.cursor(query, (value, banco.idClient))

            # banco.db.commit()

            # banco.saca(banco.idClient, value)
            # banco.db.commit()
            self.showMenssage(self.screenWithdraw, "Saque realziado com sucesso!", 1)
            self.screenWithdraw.in_value.setValue(0)
            self.openScreen(6)
        elif value <= 0:
            self.showMenssage(self.screenWithdraw, "Valor inv??lido!")
        elif value > balance:
            self.showMenssage(self.screenWithdraw, "Saldo indisponivel!")

    def btnDeposit(self):
        value = self.screenDeposit.in_value.value()

        if value > 0:
            # query = "UPDATE account SET balance = balance + %s WHERE fk_client = %s"
            # banco.db.cursor(query, (value, banco.idClient))

            mensagem = f'Deposit,{value}'
            client_socket.send(mensagem.encode())
            # mensagem = str(value)
            # client_socket.send(mensagem.encode())
            # banco.depositar(banco.idClient, value)

            # banco.db.commit()
            msg_recebida = client_socket.recv(1024).decode()
            if msg_recebida == 'True':
                self.showMenssage(self.screenDeposit, "Deposito realziado com sucesso!", 1)
                self.screenDeposit.in_value.setValue(0)
                self.openScreen(3)
            else:
                self.showMenssage(self.screenDeposit, "Erro ao depositar!")
        else:
            self.showMenssage(self.screenDeposit, "Valor inv??lido!")

    def btnTransfer(self):
        # balance = banco.getBalanceAccount(self.cpf)
        value = self.screenTransfer.in_value.value()
        destinationAccount = self.screenTransfer.in_num_account.text()

        mensagem = f'Transfer,{self.cpf},{value},{destinationAccount}'
        client_socket.send(mensagem.encode())
        # mensagem = str(self.cpf)
        # client_socket.send(mensagem.encode())
        # mensagem = str(value)
        # client_socket.send(mensagem.encode())

        # balance = client_socket.recv(1024).decode()
        msg_recebida = client_socket.recv(1024).decode()
        msg_recebida = msg_recebida.split(',')
        print(msg_recebida[3])
        balance = float(msg_recebida[3])

        if value > 0 and value <= balance:
            if destinationAccount != "":
                # mensagem = destinationAccount
                # client_socket.send(mensagem.encode())
                if msg_recebida[0] == 'True':
                    if msg_recebida[1] == 'True':
                        if msg_recebida[2] == 'True':
                            self.showMenssage(self.screenTransfer, "Transfer??ncia realizada com sucesso!", 1)
                            self.screenTransfer.in_value.setValue(0)
                            self.screenTransfer.in_num_account.setText("")
                            self.openScreen(5)
                else:
                    self.showMenssage(self.screenTransfer, "Conta n??o encontrada!")
            else:
                self.showMenssage(self.screenTransfer, "Preencha o campo conta de destino!")
        else:
            self.showMenssage(self.screenTransfer, "Valor inv??lido ou saldo indiponivel!")

    def initHistoric(self):
        mensagem = 'Historic'
        client_socket.send(mensagem.encode())

        # list_historic = list(banco.historico.getHistorico())
        self.openScreen(4)
        # msg = ""
        # for i in list_historic:
        #     msg += str(i) + "\n"
        msg = client_socket.recv(4096).decode()

        self.screenHistoric.text_historic.setText(msg)

    def btnLogin(self):
        cpf = self.screenLogin.in_cpf.text()
        password = self.screenLogin.in_password.text()
        password = MD5hash(password)

        mensagem = f'Login,{cpf},{password}'
        client_socket.send(mensagem.encode())

        if isEmpty(cpf) | isEmpty(password):
            msg = "Preencha todos os campos!"
            self.showMenssage(self.screenLogin, msg)
        else:
            # client_socket.send(str(cpf).encode())
            # client_socket.send(str(password).encode())
            lg = client_socket.recv(1024).decode()
            print("CLIENT: ", lg)
            if lg == "True":
                self.cpf = cpf
                self.screenLogin.in_cpf.setText('')
                self.screenLogin.in_password.setText('')
                self.openScreen(2)
            else:
                msg = "CPF ou senha incorretos!"
                self.showMenssage(self.screenLogin, msg)

    def btnRegistration(self):
        obj = self.screenRegistration
        name = obj.in_name.text()
        surname = obj.in_surname.text()
        cpf = obj.in_cpf.text()
        account = obj.in_account.text()
        password = obj.in_password.text()
        password = MD5hash(password)

        # mensagem = "Register"
        # client_socket.send(mensagem.encode())

        if isEmpty(name) or isEmpty(surname) or isEmpty(cpf) or isEmpty(account) or isEmpty(password):
            self.showMenssage(obj, "Preencha todos os campos!", 0)
        else:
            mensagem = f'Register,{name},{surname},{cpf},{account},{password}'
            client_socket.send(mensagem.encode())
            msg_recebida = client_socket.recv(1024).decode()
            msg_recebida = msg_recebida.split(',')
            if msg_recebida[0] == "True":
                self.showMenssage(obj, "CPF j?? cadastrado!", 0)
            else:
                if msg_recebida[1] == "True":
                    self.showMenssage(obj, "Conta j?? cadastrada!", 0)
                else:
                    # client_socket.send(name.encode())
                    # client_socket.send(surname.encode())
                    # client_socket.send(password.encode())

                    # c = Cliente(name, surname, cpf, password)
                    # banco.cria_conta(account, c)

                    obj.in_name.setText('')
                    obj.in_surname.setText('')
                    obj.in_cpf.setText('')
                    obj.in_account.setText('')
                    obj.in_password.setText('')
                    self.openScreen()

    # FUN????ES

    def showMenssage(self, obj, msg="erro", flag=0):
        if flag == 0:
            obj.frame_erro.setStyleSheet(stylePopupErro)
        else:
            obj.frame_erro.setStyleSheet(stylePopupOk)

        obj.label_erro.setText(msg)
        obj.frame_erro.show()

    # ESCONDER FRAME ERRO
    def hideFrameErro(self, obj):
        obj.frame_erro.hide()

    # BOT??O FECHAR POPUP
    def btnClosed(self, obj):
        obj.btn_x.clicked.connect(lambda: self.hideFrameErro(obj))  # CLOSED FRAME ERRO

    def btnReturn(self, i=0):
        self.QtStack.setCurrentIndex(i)

    def openScreen(self, i=0):
        if i != 0 and i != 1 and i != 4:
            # balance = banco.dic_contas[self.cpf].saldo
            # balance = banco.getBalanceAccount(self.cpf)
            mensagem = f'Balance,{self.cpf}'
            print(mensagem)
            client_socket.send(mensagem.encode())
            #client_socket.send(self.cpf.encode())
            balance = client_socket.recv(1024).decode()
            print(balance)

            self.screenWithdraw.label_balance.setText(balance)
            self.screenDash.label_balance.setText(balance)
            self.screenDeposit.label_balance.setText(balance)
            self.screenTransfer.label_balance.setText(balance)
        self.QtStack.setCurrentIndex(i)

    def desconectar(self):
        '''
            encerra a conexao com o servidor
        '''
        # print('cliente encerrado')
        client_socket.send('SAIR'.encode())
        client_socket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    # mensagem = 'SAIR'
    # client_socket.send(mensagem.encode())
    # client_socket.close()
    app.exec_()
    show_main.desconectar()
    # sys.exit(app.exec_())
    sys.exit()
