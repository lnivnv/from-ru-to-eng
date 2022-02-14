import sys
from googletrans import Translator
import sqlite3 as sql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

c = 0
class MyWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('learn')
        self.f = QPushButton('Еда')
        self.a = QPushButton('Животные')
        self.c = QPushButton('Одежда')
        self.sw = QPushButton('Сохраненные слова')
        self.translate = QPushButton("Переводчик")
        listofbtn = [self.f, self.a, self.c, self.sw, self.translate]
        for i in range(5):
            listofbtn[i].setStyleSheet("QPushButton{font-size: 14pt; background-color: rgb(235, 250, 236);"
                                       "border-radius: 15px;}")
        layout = QVBoxLayout()
        for i in range(5):
            layout.addWidget(listofbtn[i])
        self.setLayout(layout)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.mw = MyWidget()
        self.setCentralWidget(self.mw)
        self.mw.f.clicked.connect(self.food)
        self.mw.a.clicked.connect(self.animals)
        self.mw.c.clicked.connect(self.clothes)
        self.mw.sw.clicked.connect(self.savedwords)
        self.mw.translate.clicked.connect(self.trans)
        self.translator = Translator()
    def trans(self):
        self.trwidget = QWidget(self, flags=Qt.Window)
        self.trwidget.resize(600, 456)
        self.trwidget.setWindowTitle("translator")
        self.ru = QTextEdit(self.trwidget)
        self.ru.setGeometry(10, 50, 271, 311)
        self.eng = QTextEdit(self.trwidget)
        self.eng.setGeometry(320, 50, 271, 311)
        self.lru = QLabel(self.trwidget)
        self.lru.setGeometry(10, 20, 111, 21)
        self.lru.setText("Русский язык")
        self.leng = QLabel(self.trwidget)
        self.leng.setGeometry(330, 20, 231, 21)
        self.leng.setText("Английский язык")
        self.savebtn = QPushButton("сохранить", self.trwidget)
        self.savebtn.setGeometry(500, 410, 91, 41)
        self.savebtn.clicked.connect(self.addwords)
        self.tbtn = QPushButton("перевести", self.trwidget)
        self.tbtn.setGeometry(260, 370, 75, 23)
        self.tbtn.clicked.connect(self.rutoeng)
        self.trwidget.show()
    def rutoeng(self):
        mytext = self.ru.toPlainText()
        res = self.translator.translate(mytext, src='ru', dest='en')
        self.eng.setText(res.text)
        self.trwidget.show()
    def addwords(self):
        with open('mysavedwords.txt', 'a', encoding="utf-8") as file:
            file.write(f"{self.ru.toPlainText()} - {self.eng.toPlainText()}\n")
    def food(self):
        self.fwidget = QWidget(self, flags=Qt.Window)
        self.fwidget.resize(600, 600)
        self.fwidget.setWindowTitle('food')
        textlbl = QPlainTextEdit(self.fwidget)
        textlbl.appendPlainText("Ваше задание состоит в том чтобы правильно подобрать "
                                "название еды к картинке, если вы"
                                " не можете подобрать правильное название, "
                                "то нажмите на кнопку в углу, она перекнет вас в"
                                " переводчик, там вы сможете пере"
                                "вести слова и добавить в список слов, которые хотите изучить."
                                "Приятного времяпровождения!")
        textlbl.setGeometry(40, 70, 500, 180)
        textlbl.setStyleSheet("QPlainTextEdit{font-size: 14pt; background-color: rgb(235, 250, 236); "
                              "border-radius: 15px}")
        startbtn = QPushButton("Начать", self.fwidget)
        startbtn.setGeometry(230, 312, 121, 61)
        startbtn.setStyleSheet("QPushButton{font-size: 14pt; background-color: green; "
                               "border-radius: 15px}")
        startbtn.clicked.connect(self.food1)
        self.ff = []
        self.fwidget.show()
    def food1(self):
        self.fwidget.destroy()
        self.fwidget1 = QWidget(self, flags=Qt.Window)
        self.fwidget1.resize(600, 600)
        self.fwidget1.setWindowTitle('food')
        layout = QGridLayout(self.fwidget1)
        cpixmap = QPixmap("apple2.jpg")
        lbl = QLabel(self.fwidget1)
        lbl.setPixmap(cpixmap)
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)
        fruits = ["apple", "apricot", "grape"]
        for i in range(3):
            fr = QRadioButton(fruits[i], self.fwidget1)
            fr.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            fr.toggled.connect(self.food2)
            layout.addWidget(fr)
        self.fwidget1.show()
    def food2(self):
        o = self.sender().text()
        if o != "translate":
            self.ff.append(o)
        self.fwidget1.destroy()
        self.fwidget2 = QWidget(self, flags=Qt.Window)
        self.fwidget2.resize(600, 600)
        self.fwidget2.setWindowTitle('food')
        layout = QGridLayout(self.fwidget2)
        hpixmap = QPixmap("cookies2.jpg")
        lbl2 = QLabel(self.fwidget2)
        lbl2.setPixmap(hpixmap)
        lbl2.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl2)
        desserts = ["croissant", "cookies", "marshmallow"]
        for i in range(3):
            dess = QRadioButton(desserts[i], self.fwidget2)
            dess.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255);"
                               " border-radius: 3px;}")
            dess.toggled.connect(self.food3)
            layout.addWidget(dess)
        self.fwidget2.show()
    def food3(self):
        o = self.sender().text()
        if o != "translate":
            self.ff.append(self.sender().text())
        self.fwidget2.destroy()
        self.fwidget3 = QWidget(self, flags=Qt.Window)
        self.fwidget3.resize(600, 600)
        self.fwidget3.setWindowTitle('food')
        layout = QGridLayout(self.fwidget3)
        gpixmap = QPixmap("milk2.jpg")
        lbl3 = QLabel(self.fwidget3)
        lbl3.setPixmap(gpixmap)
        lbl3.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl3)
        culturedmilkfoods = ["sour cream", "sheep cheese", "milk"]
        for i in range(3):
            cmf = QRadioButton(culturedmilkfoods[i], self.fwidget3)
            cmf.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255);"
                              "border-radius: 3px;}")
            cmf.toggled.connect(self.food4)
            layout.addWidget(cmf)
        self.fwidget3.show()
    def food4(self):
        o = self.sender().text()
        if o != "translate":
            self.ff.append(self.sender().text())
        self.fwidget3.destroy()
        self.fwidget4 = QWidget(self, flags=Qt.Window)
        self.fwidget4.resize(600, 600)
        self.fwidget4.setWindowTitle('food')
        layout = QGridLayout(self.fwidget4)
        spixmap = QPixmap("potato2.jpg")
        lbl4 = QLabel(self.fwidget4)
        lbl4.setPixmap(spixmap)
        lbl4.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl4)
        vegetables = ["chick pea", "spinach", "potato"]
        for i in range(3):
            veg = QRadioButton(vegetables[i], self.fwidget4)
            veg.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255);"
                              "border-radius: 3px;}")
            veg.toggled.connect(self.food5)
            layout.addWidget(veg)
        self.fwidget4.show()
    def food5(self):
        o = self.sender().text()
        if o != "translate":
            self.ff.append(self.sender().text())
        self.fwidget4.destroy()
        self.fwidget5 = QWidget(self, flags=Qt.Window)
        self.fwidget5.resize(600, 600)
        self.fwidget5.setWindowTitle('animals')
        layout = QGridLayout(self.fwidget5)
        tpixmap = QPixmap("meat2.jpg")
        lbl5 = QLabel(self.fwidget5)
        lbl5.setPixmap(tpixmap)
        lbl5.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl5)
        beef = ["bacon", "meat", "pork"]
        for i in range(3):
            lamb = QRadioButton(beef[i], self.fwidget4)
            lamb.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255);"
                               "border-radius: 3px;}")
            lamb.toggled.connect(self.fresult)
            layout.addWidget(lamb)
        self.fwidget5.show()
    def fresult(self):
        o = self.sender().text()
        if o != "translate":
            self.ff.append(self.sender().text())
        rightansw = ["apple", 'cookies', 'milk', 'potato', 'meat']
        self.fwidget5.destroy()
        count = 0
        if o != "next":
             self.ff.append(o)
        for elem in range(5):
            if self.ff[elem] == rightansw[elem]:
                count += 1
        fres = QWidget(self, flags=Qt.Window)
        fres.resize(600, 600)
        fres.setWindowTitle('food')
        r = QLabel(fres)
        r.setText(f"Ваш результат {str(count)} из 5!")
        r.setStyleSheet("QLabel{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
        r.move(190, 270)
        con = sql.connect('food.sqlite')
        cur = con.cursor()
        cur.execute("INSERT INTO food VALUES (?, ?)", (None, count, ))
        con.commit()
        con.close()
        fres.show()
    def animals(self):
        self.awidget = QWidget(self, flags=Qt.Window)
        self.s = []
        self.awidget.resize(600, 600)
        self.awidget.setWindowTitle('animals')
        textlbl = QPlainTextEdit(self.awidget)
        textlbl.appendPlainText("Ваше задание состоит в том чтобы правильно подобрать "
                                "название животного к картинке, если вы"
                                " не можете подобрать правильное название, "
                                "то нажмите на кнопку в углу, она перекнет вас в"
                                " переводчик, там вы сможете пере"
                                "вести слова и добавить в список слов, которые хотите изучить."
                                "Приятного времяпровождения!")
        textlbl.setGeometry(40, 70, 500, 180)
        textlbl.setStyleSheet("QPlainTextEdit{font-size: 14pt; background-color: rgb(235, 250, 236); "
                              "border-radius: 15px}")
        startbtn = QPushButton("Начать", self.awidget)
        startbtn.setGeometry(230, 312, 121, 61)
        startbtn.setStyleSheet("QPushButton{font-size: 14pt; background-color: green; "
                              "border-radius: 15px}")
        startbtn.clicked.connect(self.animals1)
        self.awidget.show()
    def animals1(self):
        self.awidget.destroy()
        self.awidget1 = QWidget(self, flags=Qt.Window)
        self.awidget1.resize(600, 600)
        self.awidget1.setWindowTitle('animals')
        layout = QGridLayout(self.awidget1)
        cpixmap = QPixmap("cat.jpg")
        lbl = QLabel(self.awidget1)
        lbl.setPixmap(cpixmap)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.move(40, 70)
        layout.addWidget(lbl)
        answ = ["cat", "fox", "parrot"]
        for i in range(3):
            c1 = QRadioButton(answ[i], self.awidget1)
            c1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            c1.toggled.connect(self.animals2)
            layout.addWidget(c1)
        self.awidget1.show()
    def animals2(self):
        o = self.sender().text()
        if o != "translate":
            self.s.append(o)
        self.awidget1.destroy()
        self.awidget2 = QWidget(self, flags=Qt.Window)
        self.awidget2.resize(600, 600)
        self.awidget2.setWindowTitle('animals')
        layout = QGridLayout(self.awidget2)
        hpixmap = QPixmap("hamster2.jpg")
        lbl2 = QLabel(self.awidget2)
        lbl2.setPixmap(hpixmap)
        lbl2.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl2)
        answ = ["guinea pig", "spider", "hamster"]
        for i in range(3):
            h1 = QRadioButton(answ[i], self.awidget2)
            h1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            h1.toggled.connect(self.animals3)
            layout.addWidget(h1)
        self.awidget2.show()
    def animals3(self):
        o = self.sender().text()
        if o != "translate":
            self.s.append(self.sender().text())
        self.awidget2.destroy()
        self.awidget3 = QWidget(self, flags=Qt.Window)
        self.awidget3.resize(600, 600)
        self.awidget3.setWindowTitle('animals')
        layout = QGridLayout(self.awidget3)
        gpixmap = QPixmap("giraffe2.jpg")
        lbl3 = QLabel(self.awidget3)
        lbl3.setPixmap(gpixmap)
        lbl3.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl3)
        answ = ["giraffe", "tiger", "mouse"]
        for i in range(3):
            g1 = QRadioButton(answ[i], self.awidget3)
            g1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            g1.toggled.connect(self.animals4)
            layout.addWidget(g1)
        self.awidget3.show()
    def animals4(self):
        o = self.sender().text()
        if o != "translate":
            self.s.append(self.sender().text())
        self.awidget3.destroy()
        self.awidget4 = QWidget(self, flags=Qt.Window)
        self.awidget4.resize(600, 600)
        self.awidget4.setWindowTitle('animals')
        layout = QGridLayout(self.awidget4)
        spixmap = QPixmap("snake2.jpg")
        lbl4 = QLabel(self.awidget4)
        lbl4.setPixmap(spixmap)
        lbl4.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl4)
        answ = ["snake", "deer", "dog"]
        for i in range(3):
            s1 = QRadioButton(answ[i], self.awidget4)
            s1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            s1.toggled.connect(self.animals5)
            layout.addWidget(s1)
        self.awidget4.show()
    def animals5(self):
        o = self.sender().text()
        if o != "translate":
            self.s.append(self.sender().text())
        self.awidget4.destroy()
        self.awidget5 = QWidget(self, flags=Qt.Window)
        self.awidget5.resize(600, 600)
        self.awidget5.setWindowTitle('animals')
        layout = QGridLayout(self.awidget5)
        tpixmap = QPixmap("tiger2.jpg")
        lbl5 = QLabel(self.awidget5)
        lbl5.setPixmap(tpixmap)
        lbl5.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl5)
        answ = ["camel", "tiger", "boar"]
        for i in range(3):
            t1 = QRadioButton(answ[i], self.awidget4)
            t1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            t1.toggled.connect(self.aresult)
            layout.addWidget(t1)
        self.awidget5.show()
    def aresult(self):
        o = self.sender().text()
        if o != "translate":
            self.s.append(self.sender().text())
        rightansw = ["cat", 'hamster', 'giraffe', 'snake', 'tiger']
        self.awidget5.destroy()
        count = 0
        if o != "next":
             self.s.append(o)
        for elem in range(5):
            if self.s[elem] == rightansw[elem]:
                count += 1
        ares = QWidget(self, flags=Qt.Window)
        ares.resize(600, 600)
        ares.setWindowTitle('animals')
        r = QLabel(ares)
        r.setText(f"Ваш результат {str(count)} из 5!")
        r.setStyleSheet("QLabel{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
        r.move(190, 270)
        con = sql.connect('animals.sqlite')
        cur = con.cursor()
        cur.execute("INSERT INTO animals VALUES (?, ?)", (None, count,))
        con.commit()
        con.close()
        ares.show()
    def clothes(self):
        self.cwidget = QWidget(self, flags=Qt.Window)
        self.cwidget.resize(600, 600)
        self.cwidget.setWindowTitle('clothes')
        textlbl = QPlainTextEdit(self.cwidget)
        textlbl.appendPlainText("Ваше задание состоит в том чтобы правильно подобрать "
                                "название предмета одежды к картинке, если вы"
                                " не можете подобрать правильное название, "
                                "то нажмите на кнопку в углу, она перекнет вас в"
                                " переводчик, там вы сможете пере"
                                "вести слова и добавить в список слов, которые хотите изучить."
                                "Приятного времяпровождения!")
        textlbl.setGeometry(40, 70, 500, 180)
        textlbl.setStyleSheet("QPlainTextEdit{font-size: 14pt; background-color: rgb(235, 250, 236); "
                              "border-radius: 15px}")
        startbtn = QPushButton("Начать", self.cwidget)
        startbtn.setGeometry(230, 312, 121, 61)
        startbtn.setStyleSheet("QPushButton{font-size: 14pt; background-color: green; "
                               "border-radius: 15px}")
        self.p = []
        startbtn.clicked.connect(self.clothes1)
        self.cwidget.show()
    def clothes1(self):
        self.cwidget.destroy()
        self.cwidget1 = QWidget(self, flags=Qt.Window)
        self.cwidget1.resize(600, 600)
        self.cwidget1.setWindowTitle('clothes')
        layout = QGridLayout(self.cwidget1)
        cpixmap = QPixmap("shirt2.jpg")
        lbl = QLabel(self.cwidget1)
        lbl.setPixmap(cpixmap)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.move(40, 70)
        layout.addWidget(lbl)
        answ = ["polo shirt", "cloak", "shirt"]
        for i in range(3):
            sh1 = QRadioButton(answ[i], self.cwidget1)
            sh1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            sh1.toggled.connect(self.clothes2)
            layout.addWidget(sh1)
        self.cwidget1.show()
    def clothes2(self):
        o = self.sender().text()
        if o != "translate":
            self.p.append(o)
        self.cwidget1.destroy()
        self.cwidget2 = QWidget(self, flags=Qt.Window)
        self.cwidget2.resize(600, 600)
        self.cwidget2.setWindowTitle('clothes')
        layout = QGridLayout(self.cwidget2)
        hpixmap = QPixmap("jeans2.jpg")
        lbl2 = QLabel(self.cwidget2)
        lbl2.setPixmap(hpixmap)
        lbl2.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl2)
        answ = ["boots", "turtleneck", "jeans"]
        for i in range(3):
            je1 = QRadioButton(answ[i], self.cwidget2)
            je1.setStyleSheet(
                "QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
            je1.toggled.connect(self.clothes3)
            layout.addWidget(je1)
        self.cwidget2.show()
    def clothes3(self):
        o = self.sender().text()
        if o != "translate":
            self.p.append(self.sender().text())
        self.cwidget2.destroy()
        self.cwidget3 = QWidget(self, flags=Qt.Window)
        self.cwidget3.resize(600, 600)
        self.cwidget3.setWindowTitle('clothes')
        layout = QGridLayout(self.cwidget3)
        gpixmap = QPixmap("shorts2.jpg")
        lbl3 = QLabel(self.cwidget3)
        lbl3.setPixmap(gpixmap)
        lbl3.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl3)
        answ = ["breeches", "shorts", "sweat pants"]
        for i in range(3):
            sho1 = QRadioButton(answ[i], self.cwidget3)
            sho1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); "
                               "border-radius: 3px;}")
            sho1.toggled.connect(self.clothes4)
            layout.addWidget(sho1)
        self.cwidget3.show()
    def clothes4(self):
        o = self.sender().text()
        if o != "translate":
            self.p.append(self.sender().text())
        self.cwidget3.destroy()
        self.cwidget4 = QWidget(self, flags=Qt.Window)
        self.cwidget4.resize(600, 600)
        self.cwidget4.setWindowTitle('clothes')
        layout = QGridLayout(self.cwidget4)
        spixmap = QPixmap("skirt2.jpg")
        lbl4 = QLabel(self.cwidget4)
        lbl4.setPixmap(spixmap)
        lbl4.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl4)
        answ = ["tights", "skirt", "two-piece suit"]
        for i in range(3):
            sk1 = QRadioButton(answ[i], self.cwidget4)
            sk1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); "
                               "border-radius: 3px;}")
            sk1.toggled.connect(self.clothes5)
            layout.addWidget(sk1)
        self.cwidget4.show()
    def clothes5(self):
        o = self.sender().text()
        if o != "translate":
            self.p.append(self.sender().text())
        self.cwidget4.destroy()
        self.cwidget5 = QWidget(self, flags=Qt.Window)
        self.cwidget5.resize(600, 600)
        self.cwidget5.setWindowTitle('clothes')
        layout = QGridLayout(self.cwidget5)
        tpixmap = QPixmap("tshirt.jpg")
        lbl5 = QLabel(self.cwidget5)
        lbl5.setPixmap(tpixmap)
        lbl5.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl5)
        answ = ["braces", "frock coat", "t-shirt"]
        for i in range(3):
            ts1 = QRadioButton(answ[i], self.cwidget5)
            ts1.setStyleSheet("QRadioButton{font-size: 14pt; background-color: rgb(225, 228, 255); "
                              "border-radius: 3px;}")
            ts1.toggled.connect(self.cresult)
            layout.addWidget(ts1)
        self.cwidget5.show()
    def cresult(self):
        o = self.sender().text()
        if o != "translate":
            self.p.append(self.sender().text())
        rightansw = ["shirt", "jeans", "shorts", "skirt", "t-shirt"]
        self.cwidget5.destroy()
        count = 0
        if o != "next":
             self.p.append(o)
        for elem in range(5):
            if self.p[elem] == rightansw[elem]:
                count += 1
        cres = QWidget(self, flags=Qt.Window)
        cres.resize(600, 600)
        cres.setWindowTitle('clothes')
        r = QLabel(cres)
        r.setText(f"Ваш результат {str(count)} из 5!")
        r.setStyleSheet("QLabel{font-size: 14pt; background-color: rgb(225, 228, 255); border-radius: 3px;}")
        r.move(190, 270)
        con = sql.connect('clothes.sqlite')
        cur = con.cursor()
        cur.execute("INSERT INTO clothes VALUES (?, ?)", (None, count,))
        con.commit()
        con.close()
        cres.show()
    def savedwords(self):
        swwidget = QWidget(self, flags=Qt.Window)
        swwidget.resize(600, 600)
        swwidget.setWindowTitle('saved words')
        mysw = QPlainTextEdit(swwidget)
        savedw = open('mysavedwords.txt', "r", encoding="utf-8").read()
        mysw.setPlainText(savedw)
        mysw.resize(600, 600)
        swwidget.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication([])
    mw = MyWindow()
    mw.resize(600, 600)
    mw.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
