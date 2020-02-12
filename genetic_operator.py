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
    """

    :param chromosome:
    :return:
    """
    inserted_gene_index, source_gene_genotype, inserted_gene_genotype, segment_length =\
        random_select_operation(chromosome)

    pre_index = rd.randint(0, Parameter.gene_length - segment_length)
    post_index = pre_index + segment_length
    insert_index = rd.randint(0, Parameter.IS_elements_length - 1)
    modified_length = post_index - pre_index + insert_index

    if modified_length <= Parameter.head_length:
        inserted_gene_genotype = \
            inserted_gene_genotype[0: insert_index] + source_gene_genotype[pre_index: post_index] + \
            inserted_gene_genotype[modified_length:]
    else:
        over_length = modified_length - Parameter.head_length
        inserted_gene_genotype = \
            inserted_gene_genotype[0: insert_index] + source_gene_genotype[pre_index: post_index - over_length] + \
            inserted_gene_genotype[Parameter.head_length:]

    chromosome.genes[insert_index].genotype = inserted_gene_genotype
    chromosome.update()
    pass


def root_insert_transposition() -> None:

    pass


def random_select_operation(chromosome: c.Chromosome) -> tuple:
    inserted_gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    source_gene_genotype = chromosome.genes[rd.randint(0, Parameter.num_of_genes - 1)].genotype
    inserted_gene_genotype = chromosome.genes[inserted_gene_index].genotype
    segment_length = rd.randint(1, Parameter.IS_elements_length)
    return inserted_gene_index, source_gene_genotype, inserted_gene_genotype, segment_length

