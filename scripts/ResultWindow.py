import sqlite3

from PyQt6.QtWidgets import QWidget
import MainWindow
import StatisticFirstUI

class ResultWindow(QWidget, StatisticFirstUI.Ui_Form):
    def __init__(self, userid, anwsers, tasks, testname):
        super().__init__()
        self.setupUi(self)
        self.id = userid
        self.testname = testname

        self.rights = []
        self.wrongs = []

        try:
            for i in tasks:
                if anwsers[i[0]]:
                    if anwsers[i[0]] == i[1]:
                        self.rights.append(tasks.index(i) + 1)
                    else:
                        self.wrongs.append(tasks.index(i) + 1)
                else:
                    self.wrongs.append(tasks.index(i) + 1)

            self.wrong.setText(str(len([str(i) for i in self.wrongs])))
            self.right.setText(str(len([str(i) for i in self.rights])))
            self.wrongNumbers.setText(', '.join([str(i) for i in self.wrongs]))
        except:
            pass

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        testid = cur.execute(f'''SELECT id FROM tests WHERE testname = "{self.testname}"''').fetchone()[0]
        query = f'''UPDATE tests_solutions SET wrong_anwsers = "{" ".join([str(i) for i in self.wrongs])}"
         WHERE userid = {self.id} AND testid = {testid}'''
        cur.execute(query)
        query = f'''UPDATE tests_solutions SET right_anwsers = "{" ".join([str(i) for i in self.rights])}" 
        WHERE userid = {self.id} AND testid = {testid}'''
        cur.execute(query)
        con.commit()
        con.close()

        self.backbtn.clicked.connect(self.back)

    def back(self):
        """Метод для перенаправления на главное окно"""
        self.main = MainWindow.MainWindow(self.id)
        self.main.show()
        self.hide()