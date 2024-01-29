
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore

dastur = QApplication([])
oyna = QWidget()

oyna.setFixedSize(450, 500)
oyna.setWindowTitle("Calculator")
oyna.setStyleSheet("background-color:black")

line_edit = QLineEdit(oyna)
line_edit.setGeometry(15, 130, 415, 65)
line_edit.setFont(QFont("Arial", 20))
line_edit.setStyleSheet("background-color: white; color: black; font-size: 30px")


button_plus = QPushButton("+", oyna)
button_plus.setGeometry(330, 210, 100, 65)
button_plus.setStyleSheet("font-size: 30px;background-color: orange;color:white")

button_minus = QPushButton("-", oyna)
button_minus.setGeometry(330, 280, 100, 65)
button_minus.setStyleSheet("font-size: 30px;background-color:orange;color:white")

button_kopay = QPushButton("*", oyna)
button_kopay.setGeometry(330, 350, 100, 65)
button_kopay.setStyleSheet("font-size: 30px;background-color:orange;color:white")

button_boluv = QPushButton("/", oyna)
button_boluv.setGeometry(330, 420, 100, 65)
button_boluv.setStyleSheet("font-size: 30px;background-color:orange;color:white")

button_teng = QPushButton("=", oyna)
button_teng.setGeometry(225, 420, 100, 65)
button_teng.setStyleSheet("font-size: 30px;background-color:orange;color:white")

button_C = QPushButton("C", oyna)
button_C.setGeometry(15, 420, 100, 65)
button_C.setStyleSheet("font-size: 30px;background-color:red;color:white")

button_nol = QPushButton("0", oyna)
button_nol.setGeometry(120, 420, 100, 65)
button_nol.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_bir = QPushButton("1", oyna)
button_bir.setGeometry(15, 350, 100, 65)
button_bir.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_ikki = QPushButton("2", oyna)
button_ikki.setGeometry(120, 350, 100, 65)
button_ikki.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_uch = QPushButton("3", oyna)
button_uch.setGeometry(225, 350, 100, 65)
button_uch.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_tort = QPushButton("4", oyna)
button_tort.setGeometry(15, 280, 100, 65)
button_tort.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_besh = QPushButton("5", oyna)
button_besh.setGeometry(120, 280, 100, 65)
button_besh.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_olti = QPushButton("6", oyna)
button_olti.setGeometry(225, 280, 100, 65)
button_olti.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_etti = QPushButton("7", oyna)
button_etti.setGeometry(15, 210, 100, 65)
button_etti.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_sakkiz = QPushButton("8", oyna)
button_sakkiz.setGeometry(120, 210, 100, 65)
button_sakkiz.setStyleSheet("font-size: 30px;background-color:grey;color:white")

button_toqqiz = QPushButton("9", oyna)
button_toqqiz.setGeometry(225, 210, 100, 65)
button_toqqiz.setStyleSheet("font-size: 30px;background-color:grey;color:white;;")


def button_click(button_text):
    current_text = line_edit.text()
    new_text = current_text + button_text
    line_edit.setText(new_text)


button_nol.clicked.connect(lambda: button_click("0"))
button_bir.clicked.connect(lambda: button_click("1"))
button_ikki.clicked.connect(lambda: button_click("2"))
button_uch.clicked.connect(lambda: button_click("3"))
button_tort.clicked.connect(lambda: button_click("4"))
button_besh.clicked.connect(lambda: button_click("5"))
button_olti.clicked.connect(lambda: button_click("6"))
button_etti.clicked.connect(lambda: button_click("7"))
button_sakkiz.clicked.connect(lambda: button_click("8"))
button_toqqiz.clicked.connect(lambda: button_click("9"))

button_plus.clicked.connect(lambda: button_click("+"))
button_minus.clicked.connect(lambda: button_click("-"))
button_kopay.clicked.connect(lambda: button_click("*"))
button_boluv.clicked.connect(lambda: button_click("/"))


def calculate_result():
    try:
        result = eval(line_edit.text())
        line_edit.setText(str(result))
    except Exception as e:
        line_edit.setText("Hatolik mavjud!")


button_teng.clicked.connect(calculate_result)


def clear_input():
    line_edit.clear()

button_C.clicked.connect(clear_input)

oyna.show()
dastur.exec()

