# Form implementation generated from reading ui file 'CreatedTestStats.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(880, 576)
        self.sortby = QtWidgets.QComboBox(parent=Form)
        self.sortby.setGeometry(QtCore.QRect(140, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sortby.setFont(font)
        self.sortby.setObjectName("sortby")
        self.sortby.addItem("")
        self.sortby.addItem("")
        self.search = QtWidgets.QPushButton(parent=Form)
        self.search.setGeometry(QtCore.QRect(750, 180, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(740, 70, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.sort = QtWidgets.QPushButton(parent=Form)
        self.sort.setGeometry(QtCore.QRect(350, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sort.setFont(font)
        self.sort.setObjectName("sort")
        self.name_query = QtWidgets.QLineEdit(parent=Form)
        self.name_query.setGeometry(QtCore.QRect(720, 150, 141, 21))
        self.name_query.setObjectName("name_query")
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 681, 431))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.backbtn = QtWidgets.QPushButton(parent=Form)
        self.backbtn.setGeometry(QtCore.QRect(10, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backbtn.setFont(font)
        self.backbtn.setObjectName("backbtn")
        self.statusbar = QtWidgets.QLabel(parent=Form)
        self.statusbar.setGeometry(QtCore.QRect(750, 290, 81, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.statusbar.setPalette(palette)
        self.statusbar.setText("")
        self.statusbar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.statusbar.setWordWrap(True)
        self.statusbar.setObjectName("statusbar")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sortby.setItemText(0, _translate("Form", "Имя пользователя"))
        self.sortby.setItemText(1, _translate("Form", "Дата решения"))
        self.search.setText(_translate("Form", "Поиск"))
        self.label_2.setText(_translate("Form", "Поиск по имени пользователя:"))
        self.sort.setText(_translate("Form", "Отсортировать"))
        self.backbtn.setText(_translate("Form", "Назад"))
        self.label.setText(_translate("Form", "Сортировать по:"))
