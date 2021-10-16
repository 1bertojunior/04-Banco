from PyQt5 import QtCore, QtGui, QtWidgets


class Historic(object):
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
        self.frame_center = QtWidgets.QFrame(self.frame_content)
        self.frame_center.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_center.setMaximumSize(QtCore.QSize(400, 500))
        self.frame_center.setStyleSheet("QFrame{\n"
"    background-color: rgb(65, 65, 65);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.frame_logo = QtWidgets.QFrame(self.frame_center)
        self.frame_logo.setGeometry(QtCore.QRect(20, 5, 360, 50))
        self.frame_logo.setStyleSheet("background-image: url(:/Logo_nav/src/img/logo_nav.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 0px;\n"
"border-radius: 5px;R")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.frame_card = QtWidgets.QFrame(self.frame_center)
        self.frame_card.setGeometry(QtCore.QRect(20, 70, 360, 300))
        self.frame_card.setStyleSheet("QFrame{\n"
"    background-color: rgb(251, 195, 60);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card.setObjectName("frame_card")
        self.text_historic = QtWidgets.QTextEdit(self.frame_card)
        self.text_historic.setGeometry(QtCore.QRect(0, 0, 351, 301))
        self.text_historic.setObjectName("text_historic")
        self.horizontalLayout.addWidget(self.frame_center)
        self.verticalLayout.addWidget(self.frame_content)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_bottom.setStyleSheet("")
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_back = QtWidgets.QPushButton(self.frame_bottom)
        self.btn_back.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_back.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    background-image: url(:/Back_image/src/img/back.png);\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
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
        self.btn_back.setText("")
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_4.addWidget(self.btn_back)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Histórico"))
        self.label_erro.setText(_translate("MainWindow", "Erro"))
        self.text_historic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Inter\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Teste</p></body></html>"))


import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
