import sqlite3

from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QTableWidget, QAbstractItemView
import AuthorizationWindow
import MainWindow
import PrivateStats
import PrivateOfficeUI


class PrivateOffice(QWidget, PrivateOfficeUI.Ui_Form):
    def __init__(self, userid):
        super().__init__()
        self.setupUi(self)
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
            if temp[0] is None:
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
            self.createdtests.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        if len(data) > 0:
            result_passed = []
            for i in range(len(data)):
                row = list(data[i])
                row[1] = cur.execute(f'''SELECT username FROM users WHERE id = {row[1]}''').fetchone()[0]
                result_passed.append(row)
            self.passedtests.setRowCount(len(result_passed))
            self.passedtests.setColumnCount(len(result_passed[0]) + 1)
            self.titles = ['Название теста', 'Создатель', 'Кол-во просмотров', 'Дата создания']
            self.titles.append('')
            for i, elem in enumerate(result_passed):
                for j, val in enumerate(elem):
                    self.passedtests.setItem(i, j, QTableWidgetItem(str(val)))
                    pushButton = QPushButton('Посмотреть статистику')
                    pushButton.clicked.connect(lambda r=j, c=i: self.check_stats_passed(r, c))
                    self.passedtests.setCellWidget(i, 4, pushButton)
            self.passedtests.setHorizontalHeaderLabels(self.titles)
            self.passedtests.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        con.close()

        self.backbtn.clicked.connect(self.back)
        self.logoutbtn.clicked.connect(self.logout)

    def back(self):
        """Метод для перенаправления на главное окно"""
        self.main = MainWindow.MainWindow(self.id)
        self.main.show()
        self.hide()

    def logout(self):
        """Метод для перенаправления на первое окно"""
        self.autorize = AuthorizationWindow.AuthorizationWindow()
        self.hide()
        self.autorize.show()

    def check_stats_passed(self, r, c):
        """Метод для просмотра статистики, решёных пользователем тестов"""
        self.passed_test_stats = PrivateStats.StatsPass(self.id, self.passedtests.item(c, 0).text())
        self.hide()
        self.passed_test_stats.show()

    def check_stats_created(self, r, c):
        """Метод для просмотра статистики, созданных пользователем тестов"""
        self.crated_test_stats = PrivateStats.CreatedTestStat(self.id, self.createdtests.item(c, 0).text())
        self.hide()
        self.crated_test_stats.show()
