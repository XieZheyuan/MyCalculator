from PyQt5 import QtWidgets, QtGui
from counter import count

SYMBOLS = [[
    "平方根", "^", "平方", "ln", "取余"
], [
    "arcsin", "arccos", "arctan", "abs", "csc"
], [
    "sin", "cos", "tan", "cot", "sec"
], [
    "(", ")", "!", "立方", "开立方"
], [
    "7", "8", "9", "Del", "AC"
], [
    "4", "5", "6", "*", "/"
], [
    "1", "2", "3", "+", "-"
], [
    "0", ".", "EE", "Ans", "="
], [
    "e", "pi", ",", "Insert Function"
]
]

SYMBOLS_INPUT = {
    "平方根": "sqrt(",
    "^": "^",
    "平方": "square(",
    "ln": "ln(",
    "取余": "mod(",
    "arcsin": "asin(",
    "arccos": "acos(",
    "arctan": "atan(",
    "sin": "sin(",
    "cos": "cos(",
    "tan": "tan(",
    "cot": "cot(",
    "sec": "sec(",
    "csc": "csc(",
    "(": "(",
    ")": ")",
    "!": "fact(",
    "立方": "cube(",
    "开立方": "subtriplicate(",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/",
    "EE": "e",
    "Ans": "Val:Ans",
    "abs": "abs(",
    ".": ".",
    "e": "e",
    "pi": "pi",
    ",": ","
}

FUNCTIONS = sorted([
    "sinh", "cosh", "tanh", "asinh", "acosh", "atanh",
    "gcd", "exp", "ceil", "floor", "round", "radians", "degrees",
    "A", "C", "log10", "log2"
])


class MyCalculator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyCalculator, self).__init__(parent=parent)
        self.setWindowTitle("MyCalculator")
        self.resize(640, 480)
        self.layout_ = QtWidgets.QGridLayout()
        self.layout_.setHorizontalSpacing(0)
        self.answerLabel = QtWidgets.QLineEdit(self)
        self.answerFont = QtGui.QFont()
        self.answerFont.setPixelSize(25)
        self.answerLabel.setFont(self.answerFont)
        self.answerLabel.resize(640, 25)
        self.layout_.setSpacing(0)
        ci, cj = 0, 0
        for i in SYMBOLS:
            ci += 1
            cj = -1
            for j in i:
                cj += 1
                button = QtWidgets.QPushButton(j)

                button.clicked.connect(self.click_button(j))
                self.layout_.addWidget(button, ci, cj)

        self.setLayout(self.layout_)
        self.val_ans = 0
        with open("stylesheets/configure.txt", "r") as f:
            path = "stylesheets/" + f.read() + ".qss"

        try:
            with open(path, "r") as f:
                qss = f.read()
        except BaseException:
            QtWidgets.QMessageBox.critical(self, "MyCalculator", "This Style is not defined.")
        else:
            self.setStyleSheet(qss)

    def click_button(self, src):
        def click_func_key():
            if src == "=":
                try:
                    self.val_ans = count(self.answerLabel.text(), self.val_ans)
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, "MyCalculator", "Error Happened!\n" + str(e))
                    self.answerLabel.clear()
                    return
                self.answerLabel.setText(str(self.val_ans))
                return
            if src == "AC":
                self.answerLabel.clear()
                return
            if src == "Del":
                s = self.answerLabel.text()
                try:
                    s = s[:-2]
                except IndexError:
                    pass
                self.answerLabel.setText(s)
                return
            if src == "Insert Function":
                ans = QtWidgets.QInputDialog.getItem(self, "MyCalculator", "Choice A Function:", FUNCTIONS)
                if not ans[1]:
                    return
                text = self.answerLabel.text() + str(ans[0]) + "("
                self.answerLabel.setText(text)
                return
            text = self.answerLabel.text() + SYMBOLS_INPUT[src]
            self.answerLabel.setText(text)

        return click_func_key


if __name__ == "__main__":
    import os

    os.system("python my_calculator.py")
