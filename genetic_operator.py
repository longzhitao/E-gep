from setting import Parameter
import chromosome as c
import random as rd


def mutation(chromosome: c.Chromosome) -> c.Chromosome:
    """

    :param chromosome:
    :return:
    """
    selected_gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    gene_mutated_index = rd.randint(0, Parameter.gene_length - 1)
    if gene_mutated_index < Parameter.head_length:
        if rd.randint(0, 1) == 1:
            chromosome.genes[selected_gene_index].genotype[gene_mutated_index] = \
                Parameter.function_set[rd.randint(0, len(Parameter.function_set) - 1)]
        else:
            chromosome.genes[selected_gene_index].genotype[gene_mutated_index] = \
                Parameter.terminal_set[rd.randint(0, len(Parameter.terminal_set) - 1)]
    else:
        chromosome.genes[selected_gene_index].genotype[gene_mutated_index] = \
            Parameter.terminal_set[rd.randint(0, len(Parameter.terminal_set) - 1)]
    chromosome.update()
    return chromosome


def insert_transposition(chromosome: c.Chromosome) -> c.Chromosome:
    """

    :param chromosome:
    :return:
    """
    inserted_gene_index, source_gene_genotype, inserted_gene_genotype = \
        random_select_transposition(chromosome)

    segment_length = rd.randint(1, Parameter.IS_elements_length)
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

    chromosome.genes[inserted_gene_index].genotype = inserted_gene_genotype
    chromosome.update()
    return chromosome


def root_insert_transposition(chromosome: c.Chromosome) -> c.Chromosome:
    inserted_gene_index, source_gene_genotype, inserted_gene_genotype = \
        random_select_transposition(chromosome)

    source_select_list = list()
    for i in range(Parameter.head_length):
        if source_gene_genotype[i] in Parameter.function_set:
            source_select_list.append(i)

    if len(source_select_list) != 0:
        segment_length = rd.randint(1, Parameter.RIS_elements_length)
        pre_index = source_select_list[rd.randint(0, len(source_select_list) - 1)]
        post_index = pre_index + segment_length
        inserted_gene_genotype = \
            source_gene_genotype[pre_index: post_index] + \
            inserted_gene_genotype[0: Parameter.head_length - segment_length] + \
            inserted_gene_genotype[Parameter.head_length:]
        chromosome.genes[inserted_gene_index].genotype = inserted_gene_genotype
        chromosome.update()
    return chromosome


def gene_transposition(chromosome: c.Chromosome) -> c.Chromosome:
    pre_gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    post_gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    chromosome.genes[pre_gene_index], chromosome.genes[post_gene_index]\
        = chromosome.genes[post_gene_index], chromosome.genes[pre_gene_index]
    chromosome.update()
    return chromosome


def one_point_recombination(pre_chromosome: c.Chromosome, post_chromosome: c.Chromosome) -> c.Chromosome:
    pre_genotype = list(''.join(pre_chromosome.genotype))
    post_genotype = list(''.join(post_chromosome.genotype))
    point_index = rd.randint(0, len(pre_genotype) - 1)

    pre_genotype[point_index:], post_genotype[point_index:] = \
        post_genotype[point_index:], pre_genotype[point_index:]

    return c.Chromosome(pre_genotype)


def two_point_recombination(pre_chromosome: c.Chromosome, post_chromosome: c.Chromosome) -> c.Chromosome:
    """

    :param pre_chromosome:
    :param post_chromosome:
    :return:
    """
    pre_genotype = list(''.join(pre_chromosome.genotype))
    post_genotype = list(''.join(post_chromosome.genotype))
    pre_point_index = rd.randint(0, len(pre_genotype) - 2)
    post_point_index = rd.randint(pre_point_index + 1, len(pre_genotype) - 1)

    pre_genotype[pre_point_index: post_point_index], post_genotype[pre_point_index: post_point_index] = \
        post_genotype[pre_point_index:post_point_index], pre_genotype[pre_point_index: post_point_index]

    return c.Chromosome(pre_genotype)


def gene_recombination(pre_chromosome: c.Chromosome, post_chromosome: c.Chromosome) -> c.Chromosome:
    """

    :param pre_chromosome:
    :param post_chromosome:
    :return:
    """
    pre_genotype = list(''.join(pre_chromosome.genotype))
    post_genotype = list(''.join(post_chromosome.genotype))

    gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    point_index = gene_index * Parameter.num_of_genes

    pre_genotype[point_index:], post_genotype[point_index:] = \
        post_genotype[point_index:], pre_genotype[point_index:]

    return c.Chromosome(pre_genotype)


def random_select_transposition(chromosome: c.Chromosome) -> tuple:
    inserted_gene_index = rd.randint(0, Parameter.num_of_genes - 1)
    source_gene_genotype = chromosome.genes[rd.randint(0, Parameter.num_of_genes - 1)].genotype
    inserted_gene_genotype = chromosome.genes[inserted_gene_index].genotype

    return inserted_gene_index, source_gene_genotype, inserted_gene_genotype
