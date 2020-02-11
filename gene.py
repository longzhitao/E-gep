# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import QObject
import random as rd
from setting import Parameter


class Gene(object):
    __slots__ = ('_genotype', '_phenotype', '_fitness')
    """
        
    Attributes:
        genotype:
        phenotype:
        fitness:
    """

    def __init__(self):
        super().__init__()
        self.generate()
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
    def phenotype(self) -> list:
        return self._phenotype

    @phenotype.setter
    def phenotype(self, phenotype: list) -> None:
        self._phenotype = phenotype

    @property
    def fitness(self) -> float:
        return self._fitness

    @fitness.setter
    def fitness(self, fitness: float) -> None:
        self._fitness = fitness

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

    def update(self):
        pass
