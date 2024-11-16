import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QPushButton
import expansion
import MainWindow
import Solving

class CatalogWindow(QWidget):
    def __init__(self, userid):
        super().__init__()
        uic.loadUi('../ui/CatalogWindow.ui', self)

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = '''SELECT testname, creator, views, create_date from tests'''
        data = cur.execute(query).fetchall()
        result = []
        for i in range(len(data)):
            row = list(data[i])
            row[1] = cur.execute(f'SELECT username FROM users WHERE id={row[1]}').fetchone()[0]
            result.append(row)
        self.update_table(result, cur)
        self.id = userid
        con.close()

        self.search.clicked.connect(self.search_by_name)
        self.sort.clicked.connect(self.sorting)
        self.backbtn.clicked.connect(self.back)

    def search_by_name(self):
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
                result.append(row)
            self.update_table(result, cur)
        except:
            self.statusbar.setText('Ничего не найдено!')
        con.close()

    def sorting(self):
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
            result.append(row)
        self.update_table(result, cur)

        con.close()

    def update_table(self, data, cur):
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
        self.solve = Solving.Solving(self.id, self.tableWidget.item(c, 0).text())
        self.hide()
        self.solve.show()

    def back(self):
        self.mainwin = MainWindow.MainWindow(self.id)
        self.hide()
        self.mainwin.show()