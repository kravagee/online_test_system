# Form implementation generated from reading ui file 'Task.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(684, 510)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(100, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Image = QtWidgets.QLabel(parent=Form)
        self.Image.setGeometry(QtCore.QRect(140, 30, 400, 250))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(170, 420, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.anwser = QtWidgets.QPlainTextEdit(parent=Form)
        self.anwser.setGeometry(QtCore.QRect(220, 420, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.anwser.setFont(font)
        self.anwser.setObjectName("anwser")
        self.questiontext = QtWidgets.QLabel(parent=Form)
        self.questiontext.setGeometry(QtCore.QRect(160, 300, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.questiontext.setFont(font)
        self.questiontext.setAcceptDrops(False)
        self.questiontext.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify|QtCore.Qt.AlignmentFlag.AlignTop)
        self.questiontext.setObjectName("questiontext")
        self.savebtn = QtWidgets.QPushButton(parent=Form)
        self.savebtn.setGeometry(QtCore.QRect(530, 420, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.savebtn.setFont(font)
        self.savebtn.setObjectName("savebtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Вопрос:"))
        self.label.setText(_translate("Form", "Ответ:"))
        self.questiontext.setText(_translate("Form", "TextLabel"))
        self.savebtn.setText(_translate("Form", "Сохранить ответ"))