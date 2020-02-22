# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import QObject
import random as rd
from setting import Parameter
from algorithms import gene_read_compute_machine as grcm


class Gene(object):
    __slots__ = ('_genotype', '_value_list')
    """
        
    Attributes:
        genotype:
    """

    def __init__(self, genotype: list = None):
        if genotype is None:
            self.generate()
        else:
            self.genotype = genotype
        pass

    def __str__(self):
        return ''.join(self.genotype)

    @property
    def genotype(self) -> list:
        return self._genotype

    @genotype.setter
    def genotype(self, genotype: list) -> None:
        self._genotype = genotype

    @property
    def value_list(self) -> list:
        return self._value_list

    @value_list.setter
    def value_list(self, value):
        self._value_list = value

    def generate(self):
        """

        :return:
        """

        self.genotype = list()
        for i in range(Parameter.head_length):
            self.genotype.append(Parameter.func_ter_set[rd.randint(0, len(Parameter.func_ter_set) - 1)])
        for i in range(Parameter.tail_length):
            self.genotype.append(Parameter.terminal_set[rd.randint(0, len(Parameter.terminal_set) - 1)])
        pass
