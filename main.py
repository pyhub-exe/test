from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])

start_win = QWidget()
test_win = QWidget()

start_vertical = QVBoxLayout()
test_vertical = QVBoxLayout()
start_title = QLabel('Какой ты язык программирования?')
start_info = QLabel('!Ты сможешь узнать какой ты язык программирования за 1 минуту!')
start_button = QPushButton('Начать!')
start_button.setStyleSheet('background-color:lightblue;border-radius:4px;border:5px double blue')
start_vertical.addWidget(start_title)
start_vertical.addWidget(start_info)
start_vertical.addWidget(start_button)
start_win.setLayout(start_vertical)
test_win.setLayout(test_vertical)
def show_test():
    test_win.show()
    start_win.hide()
start_win.show()
start_button.clicked.connect(show_test)
app.exec()