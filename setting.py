# This Python file uses the following encoding: utf-8

_sample_independent_list = [101, 82, 66, 35, 31, 7, 20, 92,
                            154, 125, 85, 68, 38, 23, 10, 24,
                            83, 132, 131, 118, 90, 67, 60, 47,
                            41, 21, 16, 6, 4, 7, 14, 34,
                            45, 43, 48, 42, 28, 10, 8, 2,
                            0, 1, 5, 12, 14, 35, 46, 41,
                            30, 24, 16, 7, 4, 2, 8, 17,
                            36, 50, 62, 67, 71, 48, 28, 8,
                            13, 57, 122, 138, 103, 86, 63, 37,
                            24, 11, 15, 40, 62, 98, 124, 96,
                            66, 64, 54, 39, 21, 7, 4, 23,
                            55, 94, 96, 77, 59, 44, 47, 30,
                            16, 7, 37, 74
                            ]

_sample_independent_variable = []

for i in range(90):
    d = dict((['a', _sample_independent_list[i]],
              ['b', _sample_independent_list[i + 1]],
              ['c', _sample_independent_list[i + 2]],
              ['d', _sample_independent_list[i + 3]],
              ['e', _sample_independent_list[i + 4]],
              ['f', _sample_independent_list[i + 5]],
              ['g', _sample_independent_list[i + 6]],
              ['h', _sample_independent_list[i + 7]],
              ['i', _sample_independent_list[i + 8]],
              ['j', _sample_independent_list[i + 9]]))
    _sample_independent_variable.append(d)

_sample_dependent_variable = []

for i in range(90):
    _sample_dependent_variable.append(_sample_independent_list[i + 10])


class Parameter(object):
    __slots__ = []
    function_set = list('+-*/')  # None
    terminal_set = list('abcdefghij')  # None
    func_ter_set = list('+-*/a')
    head_length = 7  # None
    tail_length = 8  # None
    gene_length = 15  # None

    connection = ['+']
    num_of_genes = 3

    mutation_rate = 0.044
    one_point_recombination_rate = 0.3
    two_point_recombination_rate = 0.3
    gene_recombination_rate = 0.1
    IS_transposition_rate = 0.1
    RIS_transposition_rate = 0.1
    gene_transposition_rate = 0.1

    IS_elements_length = 3
    RIS_elements_length = 3

    max_fitness = 1000

    operand = {
        '+': 2,
        '-': 2,
        '*': 2,
        '/': 2,
        'S': 1,  # sin(x)
        'C': 1,  # cos(x)
        'L': 1,  # log2(x)
        'Q': 1  # sqrt(x)
    }

    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        'S': 3,
        'C': 3
    }

    population_size = 100
    constraint_constant = 1000
    num_of_samples = 90
    # sample_independent_list = [{'a': 1}]
    max_generation = 5000
    sample_dependent_variable = _sample_dependent_variable
    sample_independent_list = _sample_independent_variable


    # sample_independent_list = [{'a': 5.7695},
    #                            {'a': -4.1206},
    #                            {'a': 4.652},
    #                            {'a': -5.6193},
    #                            {'a': -3.2871},
    #                            {'a': -0.0599},
    #                            {'a': 1.1835},
    #                            {'a': -8.2814},
    #                            {'a': 4.4342},
    #                            {'a': 4.1843}]

    # sample_dependent_variable = [232.107, -56.1063, 127.968, -150.481, -27.2686,
    #                              0.943473, 5.24187, -506.651, 112.282, 95.9529]
