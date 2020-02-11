# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import QObject
import gene as g
from setting import Parameter


class Chromosome(object):
    __slots__ = ('_genes', '_genotype', '_phenotype', '_fitness')
    """

    """

    def __init__(self):
        self.generate()
        pass

    def __str__(self):
        return ''.join(self.genotype)

    @property
    def genes(self) -> list:
        return self._genes

    @genes.setter
    def genes(self, genes: list) -> None:
        self._genes = genes

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
    def fitness(self, fitness) -> None:
        self._fitness = fitness

    def generate(self):
        self.genes = list()
        self.genotype = list()
        for i in range(Parameter.num_of_genes):
            gene = g.Gene()
            self.genes.append(gene)
            self.genotype.append(''.join(gene.genotype))
            # if i is not self.num_of_genes - 1:
            #     self.genotype.append(self.connection)
        pass

    def update(self) -> None:
        self.genotype.clear()
        for i in range(Parameter.num_of_genes):
            self.genotype.append(''.join(self.genes[i].genotype))
