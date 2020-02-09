# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import QObject


class Chromosome(QObject):
    """

    """
    def __init__(self):
        super().__init__()
        self.fitness = None
        self.s = 1

