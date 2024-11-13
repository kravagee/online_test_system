import sqlite3

from PyQt6 import uic
from PIL.ImageQt import QImage
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog
import expansion
import MainWindow

class CreateWindow(QWidget):
    def __init__(self, userid):
        super().__init__()
        uic.loadUi('../ui/CreateWindow.ui', self)
        self.counter = 1
        self.task_count.display(self.counter)
        self.id = userid

        self.tasks = dict()

        self.addImage.clicked.connect(self.add_image)
        self.backbtn.clicked.connect(self.back)
        self.endEdit.clicked.connect(self.end_edit)
        self.nextTask.clicked.connect(self.next_task)

    def add_image(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.fname).scaled(self.Image.width(), self.Image.height())
        self.Image.setPixmap(self.pixmap)

    def back(self):
        try:
            anws, question, image = self.tasks[self.counter - 1]
            self.counter -= 1
            self.anwser.insertPlainText(anws)
            self.question.insertPlainText(question)
            self.pixmap = QPixmap(image).scaled(self.Image.width(), self.Image.height())
            self.Image.setPixmap(self.pixmap)
            print(self.tasks)
        except KeyError:
            self.mainwin = MainWindow.MainWindow(self.id)
            self.hide()
            self.mainwin.show()

    def end_edit(self):
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        tasks_for_db = ', '.join(['*__*'.join(i) for i in self.tasks.values()])
        query = f'''INSERT INTO tests ("testname", "tasks", creator) 
        VALUES ("{self.testname.text()}", "{tasks_for_db}", {self.id})'''
        cur.execute(query)
        con.commit()
        con.close()
        self.mainwin = MainWindow.MainWindow(self.id)
        self.hide()
        self.mainwin.show()

    def next_task(self):
        try:
            self.tasks[self.counter] = (self.question.toPlainText(), self.anwser.toPlainText(), self.fname)
            self.anwser.clear()
            self.question.clear()
            self.Image.clear()
            self.counter += 1
            self.task_count.display(self.counter)
        except:
            self.statusbar.setText('Нет картинки!')