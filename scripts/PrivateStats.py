import sqlite3

from PyQt6.QtWidgets import QWidget, QTableWidgetItem
import MainWindow
import PrivateOffice
import StatisticFirstUI
import CreatedTestStatsUI


class StatsPass(QWidget, StatisticFirstUI.Ui_Form):
    def __init__(self, userid, testname):
        super().__init__()
        self.setupUi(self)
        self.id = userid

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        testid = cur.execute(f'SELECT id FROM tests WHERE testname = "{testname}"').fetchone()[0]

        self.wrongs, self.rights = cur.execute(f'''SELECT wrong_anwsers, right_anwsers FROM tests_solutions 
        WHERE testid = {testid} AND userid = "{self.id}"''').fetchone()

        print(cur.execute(f'''SELECT wrong_anwsers, right_anwsers FROM tests_solutions 
                WHERE testid = {testid} AND userid = "{self.id}"''').fetchone())

        if self.rights and self.wrongs:
            self.wrong.setText(str(len([str(i) for i in str(self.wrongs).split(" ")])))
            self.right.setText(str(len([str(i) for i in str(self.rights).split(" ")])))
            self.wrongNumbers.setText(', '.join([str(i) for i in str(self.wrongs).split(" ")]))
        elif self.rights and not self.wrongs:
            self.right.setText(str(len([str(i) for i in str(self.rights).split(" ")])))
        elif not self.rights and self.wrongs:
            self.wrong.setText(str(len([str(i) for i in str(self.wrongs).split(" ")])))
            self.wrongNumbers.setText(', '.join([str(i) for i in str(self.wrongs).split(" ")]))

        self.backbtn.clicked.connect(self.back)

    def back(self):
        """Метод для перенаправления на окно личного кабинета"""
        self.private_office = PrivateOffice.PrivateOffice(self.id)
        self.hide()
        self.private_office.show()


class CreatedTestStat(QWidget, CreatedTestStatsUI.Ui_Form):
    def __init__(self, userid, testname):
        super().__init__()
        self.setupUi(self)
        self.id = userid
        self.testname = testname

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        self.testid = cur.execute(f'SELECT id FROM tests WHERE testname = "{self.testname}"').fetchone()[0]
        query = f'''SELECT userid, wrong_anwsers, right_anwsers, date from tests_solutions 
        WHERE testid = "{self.testid}"'''
        data = cur.execute(query).fetchall()
        result = []
        for i in range(len(data)):
            row = list(data[i])
            row[0] = cur.execute(f'SELECT username FROM users WHERE id={row[0]}').fetchone()[0]
            row[1] = ', '.join(row[1].split(' '))
            if isinstance(row[2], str):
                row[2] = ', '.join(row[2].split(' '))
            else:
                row[2] = str(row[2])
            result.append(row)
        self.update_table(result)
        con.close()

        self.search.clicked.connect(self.search_by_name)
        self.sort.clicked.connect(self.sorting)
        self.backbtn.clicked.connect(self.back)

    def search_by_name(self):
        """Метод для поиска по имени пользователя"""
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        try:
            query = f'''SELECT userid, wrong_anwsers, right_anwsers, date from tests_solutions 
                    WHERE testid = {self.testid} 
                    AND userid = (SELECT id FROM users WHERE username = "{self.name_query.text()}")'''
            data = cur.execute(query).fetchall()
            if data:
                result = []
                for i in range(len(data)):
                    row = list(data[i])
                    row[0] = cur.execute(f'SELECT username FROM users WHERE id={row[0]}').fetchone()[0]
                    row[1] = ', '.join(row[1].split(' '))
                    if isinstance(row[2], str):
                        row[2] = ', '.join(row[2].split(' '))
                    else:
                        row[2] = str(row[2])
                    result.append(row)
                self.update_table(result)
            else:
                raise Exception
        except:
            self.statusbar.setText('Ничего не найдено!')
        con.close()

    def sorting(self):
        """Метод для сортировки пользователей: по имени или по дате решения теста"""
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = f'''SELECT userid, wrong_anwsers, right_anwsers, date from tests_solutions 
                WHERE testid = "{self.testid}"'''
        data = cur.execute(query).fetchall()
        result = []
        for i in range(len(data)):
            row = list(data[i])
            row[0] = cur.execute(f'SELECT username FROM users WHERE id={row[0]}').fetchone()[0]
            row[1] = ', '.join(row[1].split(' '))
            if isinstance(row[2], str):
                row[2] = ', '.join(row[2].split(' '))
            else:
                row[2] = str(row[2])
            result.append(row)
        if self.sortby.currentText() == 'Имя пользователя':
            result = sorted(result, key=lambda x: x[0])
        elif self.sortby.currentText() == 'Дата решения':
            result = sorted(result, key=lambda x: x[-1])
        self.update_table(result)

        con.close()

    def update_table(self, data):
        """Метод для заполнения таблицы"""
        if len(data) > 0:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))
            self.titles = ['Имя пользователя', 'Неверные ответы', 'Верные ответы', 'Дата решения']
            for i, elem in enumerate(data):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.setHorizontalHeaderLabels(self.titles)

    def back(self):
        """Метод для перенаправления на главное окно"""
        self.mainwin = MainWindow.MainWindow(self.id)
        self.hide()
        self.mainwin.show()
