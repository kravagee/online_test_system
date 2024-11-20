import sqlite3

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog
import expansion
import MainWindow
import datetime as dt
import ResultWindow

USER_ANWSERS = dict()


class Task(QWidget):
    def __init__(self, question):
        super().__init__()
        uic.loadUi('../ui/Task.ui', self)

        self.question = question
        self.questiontext.setText(question[0])
        self.pixmap = QPixmap(question[-1]).scaled(self.Image.width(), self.Image.height())
        self.Image.setPixmap(self.pixmap)

        self.savebtn.clicked.connect(self.save)

    def save(self):
        USER_ANWSERS[self.question[0]] = self.anwser.toPlainText()


class Solving(QWidget):
    def __init__(self, userid, testname):
        super().__init__()
        uic.loadUi('../ui/Solving.ui', self)
        self.id = userid
        self.testname = testname

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = f'''SELECT tasks, views FROM tests WHERE testname = "{testname}"'''
        data = cur.execute(query).fetchone()
        self.views = data[-1]
        self.tasks = []
        for i in range(len(data) - 1):
            for j in data[i].split('??///??'):
                self.tasks.append(j.split('!!!!---!!!!'))

        for i in range(1, len(self.tasks) + 1):
            self.tabWidget.addTab(Task(self.tasks[i - 1]), f'Задание №{i}')

        self.backbtn.clicked.connect(self.back)


    def back(self):
        self.db_work()
        self.res = ResultWindow.ResultWindow(self.id, USER_ANWSERS, self.tasks)
        self.hide()
        self.res.show()

    def db_work(self):
        user_anws = ''
        for i in USER_ANWSERS.values():
            if i != '':
                user_anws += f'{i}#####SEPORATOR#####'
            else:
                user_anws += f' #####SEPORATOR#####'
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        testid = list(cur.execute(f'''SELECT id FROM tests WHERE testname = {self.testname}''').fetchone())[0]
        cur.execute(f'''INSERT INTO tests_solutions (testid, userid, "wrong_anwsers", "right_anwsers", 
        "anwsers", "date") VALUES ({testid}, {self.id}, "", "",
        "{user_anws}", "{dt.datetime.now().strftime("%d.%m.%Y")}")''')

        users_who = list(cur.execute(f'''SELECT users_who_passed FROM tests 
        WHERE testname="{self.testname}"''').fetchone())[0]

        new_users_who = users_who + ', ' + str(self.id)

        cur.execute(f'''UPDATE tests SET users_who_passed="{new_users_who}" WHERE testname ="{self.testname}"''')
        cur.execute(f'''UPDATE tests SET views = views + 1 WHERE testname = "{self.testname}"''')
        con.commit()
        con.close()
