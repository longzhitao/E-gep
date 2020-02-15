import math

from setting import Parameter


class GEP(object):
    def __init__(self):
        pass


def gene_read_compute_machine(sample_index: int, genotype: list) -> float:
    """

    :param sample_index:
    :param genotype:
    :return:
    """
    valid_length = get_gene_valid_length(genotype)
    index = valid_length
    try:
        while True:
            if genotype[index] in Parameter.sample_independent_list[sample_index]:
                genotype[index] = Parameter.sample_independent_list[sample_index].get(genotype[index])
            else:
                if genotype[index] == '+':
                    genotype[index] = genotype[valid_length - 1] + genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == '-':
                    genotype[index] = genotype[valid_length - 1] - genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == '*':
                    genotype[index] = genotype[valid_length - 1] * genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == '/':
                    genotype[index] = genotype[valid_length - 1] / genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == 'Q':
                    genotype[index] = genotype[valid_length] ** (1 / 2)
                    valid_length = valid_length - 1
                elif genotype[index] == 'L':
                    genotype[index] = math.log2(genotype[valid_length])
                    valid_length = valid_length - 1
                elif genotype[index] == 'S':
                    genotype[index] = math.sin(genotype[valid_length])
                    valid_length = valid_length - 1
                elif genotype[index] == 'C':
                    genotype[index] = math.cos(genotype[valid_length])
                    valid_length = valid_length - 1
            index = index - 1
            if index < 0:
                break
    except (ZeroDivisionError, ValueError) as e:
        return 0
    return genotype[0]


def get_gene_valid_length(genotype: list) -> int:
    former = 0
    latter = 0
    while True:
        if genotype[former] in Parameter.operand:
            latter = latter + Parameter.operand.get(genotype[former])
        if former == latter:
            break
        former = former + 1
    return former
