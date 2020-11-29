from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from ui import MyCalculator


app = QApplication(argv)
root = MyCalculator()
root.show()
exit(app.exec_())
