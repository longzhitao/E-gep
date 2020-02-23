# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from concurrent.futures import ThreadPoolExecutor

import gene
import setting
import chromosome
from algorithms import GEP
import algorithms


class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


temp = 0


def test():
    global temp
    for i in range(10000):
        temp = temp + 1

if __name__ == "__main__":
    # app = QApplication([])
    # window = main()
    # window.show()
    # sys.exit(app.exec_())
    g = GEP()
    g.run()
    pass







