from PyQt5 import QtCore, QtGui, QtWidgets


class Login(object): 
    # STYES
    stylePopupErro = ("background-color: rgb(239, 41, 41); border-radius: 5px;")
    stylePopupOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/src/img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(251, 195, 60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_topbar = QtWidgets.QFrame(self.centralwidget)
        self.frame_topbar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_topbar.setStyleSheet("")
        self.frame_topbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_topbar.setObjectName("frame_topbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_topbar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_erro = QtWidgets.QFrame(self.frame_topbar)
        self.frame_erro.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_erro.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_erro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_erro")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_erro)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_erro = QtWidgets.QLabel(self.frame_erro)
        self.label_erro.setStyleSheet("color:white;")
        self.label_erro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erro.setObjectName("label_erro")
        self.horizontalLayout_3.addWidget(self.label_erro)
        self.btn_x = QtWidgets.QPushButton(self.frame_erro)
        self.btn_x.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_x.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/Close_image/src/img/cil-x.png);\n"
"    background-position: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: rgb(35, 35, 35);\n"
"}")
        self.btn_x.setText("")
        self.btn_x.setObjectName("btn_x")
        self.horizontalLayout_3.addWidget(self.btn_x)
        self.horizontalLayout_2.addWidget(self.frame_erro)
        self.verticalLayout.addWidget(self.frame_topbar)
        self.frame_content = QtWidgets.QFrame(self.centralwidget)
        self.frame_content.setStyleSheet("")
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame__login_area = QtWidgets.QFrame(self.frame_content)
        self.frame__login_area.setMinimumSize(QtCore.QSize(0, 0))
        self.frame__login_area.setMaximumSize(QtCore.QSize(400, 500))
        self.frame__login_area.setStyleSheet("QFrame{\n"
"    background-color: rgb(65, 65, 65);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.frame__login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame__login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame__login_area.setObjectName("frame__login_area")
        self.frame_logo = QtWidgets.QFrame(self.frame__login_area)
        self.frame_logo.setGeometry(QtCore.QRect(20, 30, 360, 91))
        self.frame_logo.setStyleSheet("background-image: url(:/Logo/src/img/money-2.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 0px;\n"
"border-radius: 5px;R")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.in_cpf = QtWidgets.QLineEdit(self.frame__login_area)
        self.in_cpf.setGeometry(QtCore.QRect(55, 170, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_cpf.setFont(font)
        self.in_cpf.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(30,30,30);\n"
"    border: 2px solid rgb(35, 35, 35);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(251, 195, 60);\n"
"}\n"
"\n"
"\n"
"")
        self.in_cpf.setMaxLength(11)
        self.in_cpf.setObjectName("in_cpf")
        self.in_num_account = QtWidgets.QLineEdit(self.frame__login_area)
        self.in_num_account.setGeometry(QtCore.QRect(55, 230, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_num_account.setFont(font)
        self.in_num_account.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(30,30,30);\n"
"    border: 2px solid rgb(35, 35, 35);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(251, 195, 60);\n"
"}\n"
"\n"
"\n"
"")
        self.in_num_account.setMaxLength(8)
        self.in_num_account.setObjectName("in_num_account")
        self.btn_login = QtWidgets.QPushButton(self.frame__login_area)
        self.btn_login.setGeometry(QtCore.QRect(55, 300, 280, 50))
        self.btn_login.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(251, 195, 60);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"}\n"
"")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.frame__login_area)
        self.verticalLayout.addWidget(self.frame_content)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_bottom.setStyleSheet("")
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_register = QtWidgets.QPushButton(self.frame_bottom)
        self.btn_register.setMaximumSize(QtCore.QSize(280, 20))
        self.btn_register.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: rgb(35, 35, 35);\n"
"}")
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout_4.addWidget(self.btn_register)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # ALTERAÇÕES
        self.btn_x.clicked.connect(lambda: self.hideFrameErro()) # CLOSED FRAME ERRO

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #FUNÇÕES
    # ESCONDER FRAME ERRO
    def hideFrameErro(self):
        self.frame_erro.hide()
    def isEmpty(self,arg):
        return arg == ""
    # CHECAR CAMPOS LOGIN
    def checkFields(self):
        cpf = self.in_cpf.text()
        account = self.in_num_account.text()

        def showMenssage(msg):
            self.label_erro.setText(msg)
            self.frame_erro.show()

        if self.isEmpty(cpf) | self.isEmpty(account):
            msg = "Preencha todos os campos!"
            self.frame_erro.setStyleSheet(self.stylePopupErro)
            showMenssage(msg)
        else:
            msg = "Logado com sucesso!"
            self.frame_erro.setStyleSheet(self.stylePopupOk)
            showMenssage(msg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_erro.setText(_translate("MainWindow", "Erro"))
        self.in_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.in_num_account.setPlaceholderText(_translate("MainWindow", "N conta"))
        self.btn_login.setText(_translate("MainWindow", "Entrar"))
        self.btn_register.setText(_translate("MainWindow", "Cadastro"))


import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())