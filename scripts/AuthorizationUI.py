# Form implementation generated from reading ui file 'Authorization.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 510)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.loginbtn = QtWidgets.QPushButton(parent=Form)
        self.loginbtn.setGeometry(QtCore.QRect(110, 170, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginbtn.setFont(font)
        self.loginbtn.setObjectName("loginbtn")
        self.registerbtn = QtWidgets.QPushButton(parent=Form)
        self.registerbtn.setGeometry(QtCore.QRect(110, 270, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.registerbtn.setFont(font)
        self.registerbtn.setObjectName("registerbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Добро пожаловать в систему для онлайн тестирования! Чтобы продолжить войдите или создайте аккаунт!"))
        self.loginbtn.setText(_translate("Form", "Авторизация"))
        self.registerbtn.setText(_translate("Form", "Регистрация"))
