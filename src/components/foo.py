from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QPushButton

btn_style = """
QPushButton {
    color: rgb(36, 36, 36);
    background-color: rgb(222, 222, 222);
    font-family: times;
    font-size:11px;
    border-color: #2752B8;
}

QPushButton:pressed {
    color: #fff;
    cursor: pointer;
    margin: 2px;
    height: 55px;
    text-align:center;
    border: none;
}

"""


class Foo(QFrame):

    def __init__(self, parent):
        super(Foo, self).__init__()

        self.home = QPushButton("Home", self)
        self.home.setGeometry(QRect(0, 0, 75, 23))
        font = QFont()
        # font.setFamily(u"times")
        font.setBold(True)
        # font.setWeight(QFont.Weight(75))
        # self.home.setFont(font)
        self.home.setStyleSheet(btn_style)

        self.accounts = QPushButton("accounts", self)
        self.accounts.setGeometry(QRect(70, 0, 75, 23))
        self.accounts.setFont(font)
        self.accounts.setStyleSheet(btn_style)

        self.employee = QPushButton("Employees", self)
        self.employee.setGeometry(QRect(140, 0, 75, 23))
        self.employee.setFont(font)
        self.employee.setStyleSheet(btn_style)

        self.clients = QPushButton("Clients", self)
        self.clients.setGeometry(QRect(210, 0, 75, 23))
        self.clients.setFont(font)
        self.clients.setStyleSheet(btn_style)

        self.dep = QPushButton("Departments", self)
        self.dep.setGeometry(QRect(280, 0, 75, 23))
        self.dep.setFont(font)
        self.dep.setStyleSheet(btn_style)
