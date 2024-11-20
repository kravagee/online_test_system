import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QPushButton
import AuthorizationWindow
import expansion
import MainWindow

class PrivateOffice(QWidget):
    def __init__(self, userid):
        super().__init__()
        uic.loadUi('../ui/PrivateOffice.ui', self)
        self.id = userid

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = '''SELECT testname, creator, views, create_date from tests'''
        data = cur.execute(query).fetchall()
        data_cop = data.copy()
        result = []
        for i in range(len(data_cop)):
            row = list(data_cop[i])
            creator_id = row[1]
            row[1] = cur.execute(f'SELECT username FROM users WHERE id={row[1]}').fetchone()[0]
            temp = list(cur.execute(f'''SELECT users_who_passed FROM tests WHERE testname="{row[0]}"''').fetchone())
            if temp[0] != None:
                print(temp[0].split(', '))
                if not (str(self.id) in temp[0].split(', ')):
                    data.remove(data_cop[i])
                if creator_id == self.id:
                    result.append(row)
        if len(result) > 0:
            self.createdtests.setRowCount(len(result))
            self.createdtests.setColumnCount(len(result[0]) + 1)
            self.titles = ['Название теста', 'Создатель', 'Кол-во просмотров', 'Дата создания']
            self.titles.append('')
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.createdtests.setItem(i, j, QTableWidgetItem(str(val)))
                    pushButton = QPushButton('Посмотреть статистику')
                    pushButton.clicked.connect(lambda r=j, c=i: self.check_stats_created(r, c))
                    self.createdtests.setCellWidget(i, 4, pushButton)
            self.createdtests.setHorizontalHeaderLabels(self.titles)

        if len(data) > 0:
            self.passedtests.setRowCount(len(data))
            self.passedtests.setColumnCount(len(data[0]) + 1)
            self.titles = ['Название теста', 'Создатель', 'Кол-во просмотров', 'Дата создания']
            self.titles.append('')
            for i, elem in enumerate(data):
                for j, val in enumerate(elem):
                    self.passedtests.setItem(i, j, QTableWidgetItem(str(val)))
                    pushButton = QPushButton('Посмотреть статистику')
                    pushButton.clicked.connect(lambda r=j, c=i: self.check_stats_passed(r, c))
                    self.passedtests.setCellWidget(i, 4, pushButton)
            self.passedtests.setHorizontalHeaderLabels(self.titles)
        con.close()

        self.backbtn.clicked.connect(self.back)
        self.logoutbtn.clicked.connect(self.logout)


    def back(self):
        self.main = MainWindow.MainWindow(self.id)
        self.main.show()
        self.hide()

    def logout(self):
        pass

    def check_stats_passed(self, r, c):
        print(self.passedtests.item(c, 0).text())

    def check_stats_created(self, r, c):
        print(self.createdtests.item(c, 0).text())