# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow

import gene
import setting
import chromosome
import genetic_operator as go


class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


if __name__ == "__main__":
    # app = QApplication([])
    # window = main()
    # window.show()
    # sys.exit(app.exec_())
    c = chromosome.Chromosome()
    print(c.genotype)
    go.mutation(c)
    print(c.genotype)
    go.insert_transposition(c)
    print(c.genotype)
    go.root_insert_transposition(c)
    print(c.genotype)
    go.gene_transposition(c)
    print(c.genotype)







