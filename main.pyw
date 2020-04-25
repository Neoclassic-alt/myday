import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QToolTip
from PyQt5.QtGui import QIcon, QBrush, QColor, QPixmap, QFont
import ex_functions # особые функции

import design, files, redactordesign, tagslist
# design - файл дизайна программы, files - функции с файлами,
# redactordesign - дизайн редактора, tagslist - список тегов

class Example(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(AppIcon)
        self.ListOfPosts.addItems(files.labels)
        self.ListOfPosts.itemClicked.connect(self.printPost)
        self.ListOfPosts.scrollToBottom()
        self.textEdit.setPlaceholderText("Запись не выбрана")
        self.RedactorButton.clicked.connect(self.openRedactorWindow)
        self.DeleteButton.clicked.connect(self.delete)
        self.NewPostButton.clicked.connect(self.openCreateWindow)
        self.listOfTagsButton.clicked.connect(self.openTagsWindow)
        self.colorOfItems = QColor(225, 255, 209)
        self.painted = False
        self._setFont()

    def _setFont(self):
        font = QFont("Consolas", 10)
        for i in range(0, self.ListOfPosts.count()):
            self.ListOfPosts.item(i).setFont(font)

    def setButtonActive(self, bool):
        self.RedactorButton.setEnabled(bool)
        self.DeleteButton.setEnabled(bool)
        self.lineEdit.setEnabled(bool)

    def printPost(self):
        self.t = self.ListOfPosts.currentRow()
        self.textEdit.setText(files.nameread(self.t))

        tags = files.readtags(self.t)
        self.lineEdit.setText(tags)
        self.setButtonActive(True)
        c = files.readdate(self.t)
        if len(c) == 1:
            self.Date.setText(c[0])
            self.pixmapLabel.clear()
        if len(c) == 2:
            self.Date.setToolTip("Отредактировано: " + c[1])
            self.pixmapLabel.setPixmap(QPixmap("images/ei.png"))

    def openRedactorWindow(self):
        self.Redactor = Redactor(self.t)
        self.Redactor.show()
        self.Redactor.setWindowTitle("Редактировать запись")

    def openCreateWindow(self):
        self.Creator = Create()
        self.Creator.show()
        self.Creator.setWindowTitle("Новая запись")
    
    def update(self, row, text_label, post_text, tags, currentDate):
        self.ListOfPosts.item(row).setText(text_label)
        self.textEdit.setText(post_text)
        self.lineEdit.setText(tags)
        self.Date.setText(currentDate[0])
        self.Date.setToolTip("Отредактировано: " + currentDate[1])
        self.pixmapLabel.setPixmap(QPixmap("images/ei.png"))

    def delete(self):
        reply = QMessageBox.question(self, "Сообщение", 
                                         "Вы точно хотите удалить файл?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            files.delete(self.t)
            self.ListOfPosts.takeItem(self.t)
            self.textEdit.clear()
            self.lineEdit.clear()
            self.setButtonActive(False)
            self.ListOfPosts.clearSelection()
            self.Date.clear()
            self.pixmapLabel.clear()

    def acceptNew(self, name, text, tags, date):
        self.ListOfPosts.addItem(name)
        self.ListOfPosts.setCurrentRow(len(files.names)-1)
        self.ListOfPosts.item(len(files.names)-1).setFont(QFont("Consolas", 10))
        self.textEdit.setText(text)
        self.lineEdit.setText(tags)
        self.Date.setText(date)
        self.setButtonActive(True)

    def openTagsWindow(self):
        if self.painted == False:
            self.tagsl = TagsList()
            self.tagsl.show()
        else:
            self.depaint()

    def paintItems(self, listOfItems):
        for i in listOfItems:
            self.ListOfPosts.item(i).setBackground(QBrush(self.colorOfItems))
        self.painted = True
        self.listOfTagsButton.setText("Отменить выделение записей")
        self.ListOfPosts.clearSelection()
        

    def depaint(self):
        i = 0
        while i < self.ListOfPosts.count():
            self.ListOfPosts.item(i).setBackground(QBrush(QColor(255, 255, 255)))
            i = i + 1
        self.painted = False
        self.listOfTagsButton.setText("Список тегов")

class Redactor(QtWidgets.QMainWindow, redactordesign.Ui_RedactorWindow):
    def __init__(self, t):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(AppIcon)
        self.num = t
        label = files.names[self.num]
        self.label.setText(label)
        self.textRedactor.setText(files.nameread(self.num))
        self.tagsEdit.setText(files.readtags(self.num))
        self.tagsEdit.setPlaceholderText("Теги помогают категоризировать записи")
        self.closeButton.clicked.connect(self.m_close)
        self.SaveButton.clicked.connect(self.save)

    def m_close(self):
        if (self.label.text() != files.names[self.num] or
           self.textRedactor.toPlainText() != files.nameread(self.num) or
           self.tagsEdit.text() != files.readtags(self.num)):
            text_reply = "Вы точно хотите закрыть окно?\nВы потеряете несохранённые данные."
            reply = QMessageBox()
            reply.setWindowTitle("Сообщение")
            reply.setText(text_reply)
            reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            reply.setDefaultButton(QMessageBox.No)
            reply.setWindowIcon(AppIcon)
            reply.setIconPixmap(QPixmap("images/attention.png"))
            ret = reply.exec_()

            if ret == QMessageBox.Yes:
                self.close()
        else:
            self.close()

    def save(self):
        if self.label.text() != "" and self.textRedactor.toPlainText() != "":
            files.changename(self.num, self.label.text())
            files.changetext(self.num, self.textRedactor.toPlainText())
            files.changetags(self.num, self.tagsEdit.text())
            c = files.changedate(self.num, ex_functions.getNowTime())
            ex.update(self.num, self.label.text(), 
                      self.textRedactor.toPlainText(), self.tagsEdit.text(), c)
            self.close()
        else:
            text_reply = "Заголовок и текст записи не должны быть пустыми"
            QMessageBox.about(self, "Сообщение", text_reply)

class Create(QtWidgets.QMainWindow, redactordesign.Ui_RedactorWindow):
    # собственно, то же окно, но только на создание
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(AppIcon)
        self.closeButton.clicked.connect(self.m_close)
        self.SaveButton.clicked.connect(self.newPost)

    def m_close(self):
        text_reply = "Вы точно хотите закрыть окно?\nВы потеряете несохранённые данные."
        if (self.label.text() != "" or 
            self.textRedactor.toPlainText() != "" or self.tagsEdit.text() != ""):
            reply = QMessageBox()
            reply.setWindowTitle("Сообщение")
            reply.setText(text_reply)
            reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            reply.setDefaultButton(QMessageBox.No)
            reply.setWindowIcon(AppIcon)
            reply.setIconPixmap(QPixmap("images/attention.png"))
            ret = reply.exec_()

            if ret == QMessageBox.Yes:
                self.close()
        else:
            self.close()

    def newPost(self):
        if self.label.text() != "" and self.textRedactor.toPlainText() != "":
            self.t = files.lastRecordNum()
            files.createNewPost(self.t+1, self.label.text(), 
                                self.textRedactor.toPlainText(), 
                                self.tagsEdit.text(), ex_functions.getNowTime())
            ex.acceptNew(self.label.text(), self.textRedactor.toPlainText(),
                           self.tagsEdit.text(), ex_functions.getNowTime())
            self.close()
        else:
            text_reply = "Заголовок и текст записи не должны быть пустыми"
            QMessageBox.about(self, "Сообщение", text_reply)

class TagsList(QtWidgets.QMainWindow, tagslist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(AppIcon)
        self.closeButton.clicked.connect(self.close)
        t = ex_functions.tagsProcessing()
        self.listOfTags.addItems(t.printTags())
        self.listOfTags.itemSelectionChanged.connect(self.update)
        self.primeButton.clicked.connect(self.select)

    def update(self):
        if len(self.listOfTags.selectedItems()) == 0:
            self.primeButton.setEnabled(False)
        elif len(self.listOfTags.selectedItems()) == 1:
            self.primeButton.setEnabled(True)
            self.primeButton.setText("Выделить записи с этим тегом")
        else:
            self.primeButton.setEnabled(True)
            self.primeButton.setText("Выделить записи с этими тегами")

    def select(self):
        select_texts = []
        for i in self.listOfTags.selectedIndexes():
            select_texts.append(i.row())
        t = ex_functions.tagsProcessing()
        t.printTags()
        paint_index = t.selectPosts(select_texts)
        list(paint_index)
        ex.paintItems(paint_index)
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    AppIcon = QIcon("images/book_pix.png")
    ex = Example()
    ex.show()
    sys.exit(app.exec_())