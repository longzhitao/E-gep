# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow

import gene


class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


if __name__ == "__main__":
    # app = QApplication([])
    # window = main()
    # window.show()
    # sys.exit(app.exec_())
    g = gene.Gene()
    print(g)
    g.mutation()
    print(g)
