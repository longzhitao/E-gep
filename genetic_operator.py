from setting import Parameter
import chromosome as c
import random as rd


def mutation(chromosome: c.Chromosome) -> None:
    """

    :param chromosome:
    :return:
    """
    selected_gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    gene_mutated_index = rd.randint(0, Parameter.gene_length - 1)
    if gene_mutated_index < Parameter.head_length:
        chromosome.genes[selected_gene_index].genotype[gene_mutated_index] = \
            Parameter.func_ter_set[rd.randint(0, len(Parameter.func_ter_set) - 1)]
    else:
        chromosome.genes[selected_gene_index].genotype[gene_mutated_index] = \
            Parameter.terminal_set[rd.randint(0, len(Parameter.terminal_set) - 1)]
    chromosome.update()
    pass


def insert_transposition(chromosome: c.Chromosome) -> None:

    pass

