import sqlite3

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
import MainWindow
import datetime as dt
import CreateWindowUI


class CreateWindow(QWidget, CreateWindowUI.Ui_Form):
    def __init__(self, userid):
        super().__init__()
        self.setupUi(self)
        self.counter = 1
        self.task_count.display(self.counter)
        self.id = userid

        self.tasks = dict()

        self.addImage.clicked.connect(self.add_image)
        self.backbtn.clicked.connect(self.back)
        self.endEdit.clicked.connect(self.end_edit)
        self.nextTask.clicked.connect(self.next_task)

    def add_image(self):
        """Метод для добавления картинки"""
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.fname).scaled(self.Image.width(), self.Image.height())
        self.Image.setPixmap(self.pixmap)

    def back(self):
        """Метод возвращения назад"""
        try:
            anws, question, image = self.tasks[self.counter - 1]
            self.counter -= 1
            self.anwser.insertPlainText(anws)
            self.question.insertPlainText(question)
            self.pixmap = QPixmap(image).scaled(self.Image.width(), self.Image.height())
            self.Image.setPixmap(self.pixmap)
            print(self.tasks)
            self.statusbar.setText('')
        except KeyError:
            self.mainwin = MainWindow.MainWindow(self.id)
            self.hide()
            self.mainwin.show()

    def end_edit(self):
        """Метод для завершения создания теста"""
        if self.question.toPlainText() != '' and self.anwser.toPlainText() != '':
            self.tasks[self.counter] = (self.question.toPlainText(), self.anwser.toPlainText(), self.fname)
            con = sqlite3.connect('../db/users.db')
            cur = con.cursor()
            if self.testname.text() != '':
                query = cur.execute(f'''SELECT * FROM tests WHERE testname = "{self.testname.text()}"''').fetchall()
                if query:
                    self.statusbar.setText('Такое имя теста уже занято!')
                tasks_for_db = '??///?? '.join(['!!!!---!!!!'.join(i) for i in self.tasks.values()])
                query = f'''INSERT INTO tests ("testname", "tasks", creator, views, "create_date", 
                        "users_who_passed") 
                        VALUES ("{self.testname.text()}", "{tasks_for_db}", {self.id}, {0}, 
                        "{dt.datetime.now().strftime("%d.%m.%Y")}", "")'''
                cur.execute(query)
                con.commit()
                con.close()
                self.mainwin = MainWindow.MainWindow(self.id)
                self.hide()
                self.mainwin.show()
            else:
                self.message()
                self.statusbar.setText('Дайте имя тесту!')
        else:
            self.message()
            self.statusbar.setText('Недостаточно данных!')

    def next_task(self):
        """Метод для переключения между задачами теста"""
        try:
            self.tasks[self.counter] = (self.question.toPlainText(), self.anwser.toPlainText(), self.fname)
            self.anwser.clear()
            self.question.clear()
            self.Image.clear()
            self.counter += 1
            self.task_count.display(self.counter)
            self.statusbar.setText('')
        except:
            self.message()
            self.statusbar.setText('Недостаточно данных!')

    def message(self):
        msg = QMessageBox(self)
        msg.setText('Подсказка:\nОБЯЗАТЕЛЬНО добавьте картинку, \nнапишите текст для вопроса и ответ.'
                    '\nТакже не забудьте указать имя теста!')
        button = msg.exec()
        if button == QMessageBox.StandardButton.Ok:
            print('OK')
