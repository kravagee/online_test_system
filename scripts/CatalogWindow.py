import sqlite3

from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QPushButton
import MainWindow
import Solving
import CatalogUI


class CatalogWindow(QWidget, CatalogUI.Ui_Form):
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
            row[1] = cur.execute(f'SELECT username FROM users WHERE id={row[1]}').fetchone()[0]
            temp = list(cur.execute(f'''SELECT users_who_passed FROM tests WHERE testname="{row[0]}"''').fetchone())
            if temp[0] != None:
                print(temp[0].split(', '))
                if not str(self.id) in temp[0].split(', '):
                    result.append(row)
                else:
                    data.remove(data_cop[i])
            else:
                result.append(row)
        self.update_table(result)
        self.id = userid
        con.close()

        self.search.clicked.connect(self.search_by_name)
        self.sort.clicked.connect(self.sorting)
        self.backbtn.clicked.connect(self.back)

    def search_by_name(self):
        """Метод для поиска тестов по названию"""
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        try:
            query = f'''SELECT testname, creator, views, create_date 
            from tests WHERE testname = "{self.name_query.text()}"'''
            data = cur.execute(query).fetchall()
            result = []
            for i in range(len(data)):
                row = list(data[i])
                row[1] = cur.execute(f'SELECT username FROM users WHERE id={row[1]}').fetchone()[0]
                temp = cur.execute(f'''SELECT users_who_passed FROM tests WHERE testname="{row[0]}"''').fetchone()
                if temp:
                    if not self.id in temp[0].split(', '):
                        result.append(row)
                else:
                    result.append(row)
            self.update_table(result)
        except:
            self.statusbar.setText('Ничего не найдено!')
        con.close()

    def sorting(self):
        """Метод для сортировки тестов по популярности, названию и дате создания"""
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        if self.sortby.currentText() == 'Популярность':
            query = '''SELECT testname, creator, views, create_date from tests ORDER BY views'''
        elif self.sortby.currentText() == 'Название':
            query = '''SELECT testname, creator, views, create_date from tests ORDER BY testname'''
        else:
            query = '''SELECT testname, creator, views, create_date from tests ORDER BY create_date'''
        data = cur.execute(query).fetchall()
        result = []
        for i in range(len(data)):
            row = list(data[i])
            row[1] = cur.execute(f'SELECT username FROM users WHERE id={row[1]}').fetchone()[0]
            temp = cur.execute(f'''SELECT users_who_passed FROM tests WHERE testname="{row[0]}"''').fetchone()
            if temp:
                if not self.id in temp[0].split(', '):
                    result.append(row)
            else:
                result.append(row)
        self.update_table(result)

        con.close()

    def update_table(self, data):
        """Метод для заполнения таблицы"""
        if len(data) > 0:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]) + 1)
            self.titles = ['Название теста', 'Создатель', 'Кол-во просмотров', 'Дата создания']
            self.titles.append('')
            for i, elem in enumerate(data):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                    pushButton = QPushButton('Открыть')
                    self.tableWidget.setCellWidget(i, 4, pushButton)
                    pushButton.clicked.connect(lambda r=j, c=i: self.go_to(r, c))
            self.tableWidget.setHorizontalHeaderLabels(self.titles)

    def go_to(self, r, c):
        """Метод для перенаправления на окно с решением выбранного теста"""
        self.solve = Solving.Solving(self.id, self.tableWidget.item(c, 0).text())
        self.hide()
        self.solve.show()

    def back(self):
        """Метод для перенаправления на главное"""
        self.mainwin = MainWindow.MainWindow(self.id)
        self.hide()
        self.mainwin.show()
