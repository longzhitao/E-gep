# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import QObject
import random as rd


class Gene(object):
    __slots__ = ('_genotype', '_phenotype', '_fitness')
    """
    Class Attributes:
        function_set:
        terminal_set:
        head_length:
        tail_length:
        gene_length:
        
    Attributes:
        genotype:
        phenotype:
        fitness:
    """
    function_set = list('+-*/')  # None
    terminal_set = list('a')  # None
    func_ter_set = list('+-*/a')
    head_length = 3  # None
    tail_length = 4  # None
    gene_length = 7  # None

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
        for i in range(self.head_length):
            self.genotype.append(self.func_ter_set[rd.randint(0, len(self.func_ter_set) - 1)])
        for i in range(self.tail_length):
            self.genotype.append(self.terminal_set[rd.randint(0, len(self.terminal_set) - 1)])
        pass

    def mutation(self):
        """

        :return:
        """
        self.genotype[rd.randint(0, self.gene_length - 1)] = \
            self.func_ter_set[len(self.func_ter_set) - 1]
        pass
