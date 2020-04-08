import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):

        print("clicked", v)
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "C":
            self.results.setText("")
        elif v == "CE":
            current_value = self.results.text()
            new_value = current_value[:-1]
            self.results.setText(new_value)
        elif v == "√":
            current_value = float(eval(self.results.text()))
            new_value = math.sqrt(current_value)
            self.results.setText(str(new_value))
        elif v == "^":
            current_value = self.results.text()
            new_value = current_value + "**"
            self.results.setText(new_value)

        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.create_app()

    def create_app(self):

        # Create grid
        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["C", "CE", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   ".", 0, "^", "√",
                   "="]

        row = 1
        col = 1

        grid.addWidget(results, 0, 0, 1, 4)

        for button in buttons:
            if col > 3:
                row += 1
                col = 0

            buttonObject = Button(button, results)

            if buttonObject.text == "=":
                grid.addWidget(buttonObject.b, row, col, 1, 4)
            else:
                grid.addWidget(buttonObject.b, row, col, 1, 1)

            col += 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())