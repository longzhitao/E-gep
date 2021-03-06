# This Python file uses the following encoding: utf-8
import gene as g
from setting import Parameter


class Chromosome(object):
    __slots__ = ('_genes', '_genotype', '_fitness')
    """

    """

    def __init__(self, genotype: list = None):
        if genotype is None:
            self.generate()
        else:
            self.genotype = list()
            self.genes = list()
            for i in range(Parameter.num_of_genes):
                gene = g.Gene(genotype[i * Parameter.gene_length: i * Parameter.gene_length + Parameter.gene_length])
                self.genes.append(gene)
                self.genotype.append(''.join(gene.genotype))
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
    def fitness(self) -> float:
        return self._fitness

    @fitness.setter
    def fitness(self, fitness: float) -> None:
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




