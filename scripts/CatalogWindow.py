import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QPushButton
import expansion
import MainWindow

class CatalogWindow(QWidget):
    def __init__(self, userid):
        super().__init__()
        uic.loadUi('../ui/CatalogWindow.ui', self)

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = '''SELECT testname, creator, views, create_date from tests'''
        data = cur.execute(query).fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]) + 1)
        self.titles = [description[0] for description in cur.description]
        self.titles.append('')
        for i, elem in enumerate(data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                pushButton = QPushButton('Открыть')
                self.tableWidget.setCellWidget(i, 4, pushButton)
                pushButton.clicked.connect(lambda r=j, c=i: self.go_to(r, c))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        con.close()

        self.search.clicked.connect(self.search_by_name)
        self.sortby.clicked.connect(self.sorting)

    def search_by_name(self):
        # Позже задумаюсь о вынесении генерации таблицы в отдельный метод, для оптимизации
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        try:
            query = f'''SELECT testname, creator, views, create_date 
            from tests WHERE testname = "{self.name_query.text()}"'''
            data = cur.execute(query).fetchall()
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]) + 1)
            self.titles = [description[0] for description in cur.description]
            self.titles.append('')
            for i, elem in enumerate(data):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                    pushButton = QPushButton('Открыть')
                    self.tableWidget.setCellWidget(i, 4, pushButton)
                    pushButton.clicked.connect(lambda r=j, c=i: self.go_to(r, c))
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
        except:
            self.statusbar.setText('Ничего не найдено!')
        con.close()

    def sorting(self):
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = '''SELECT testname, creator, views, create_date from tests SORT BY'''
        data = cur.execute(query).fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]) + 1)
        self.titles = [description[0] for description in cur.description]
        self.titles.append('')
        for i, elem in enumerate(data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                pushButton = QPushButton('Открыть')
                self.tableWidget.setCellWidget(i, 4, pushButton)
                pushButton.clicked.connect(lambda r=j, c=i: self.go_to(r, c))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        con.close()

    def go_to(self, r, c):
        print(self.tableWidget.item(c, 0).text())