from PyQt6.QtWidgets import QApplication, QMainWindow
import MainWindow

import random
import os

ui = MainWindow.Ui_Dialog()
app = QApplication([])
win = QMainWindow()
ui.setupUi(win)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

#ui elements
def generate():
    global letters
    global numbers
    global symbols
    global password
    
    print("Generating Password")
    l = ui.length.value()
    u = ui.doUpperCase.isChecked()
    n = ui.doNumbers.isChecked()
    s = ui.doSymbols.isChecked()

    choices = []
    choices.extend(letters)
    
    if u == True:
        choices.extend(letter.upper() for letter in letters)
    if n == True:
        choices.extend(numbers)
    if s == True:
        choices.extend(symbols)
    
    print(choices)
    password = ''.join(random.choice(choices) for _ in range(l))
    print(password)
    ui.plainTextEdit.setPlainText(password)
    
ui.generate.clicked.connect(lambda:generate())

win.show()
app.exec()