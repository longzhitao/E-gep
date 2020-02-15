# This Python file uses the following encoding: utf-8
class Parameter(object):
    __slots__ = []
    function_set = list('+-*/')  # None
    terminal_set = list('a')  # None
    func_ter_set = list('+-*/a')
    head_length = 3  # None
    tail_length = 4  # None
    gene_length = 7  # None

    connection = ['+']
    num_of_genes = 3
    IS_elements_length = 3
    RIS_elements_length = 3

    operand = {
        '+': 2,
        '-': 2,
        '*': 2,
        '/': 2,
        'S': 1,  # sin(x)
        'C': 1,  # cos(x)
        'L': 1,  # log2(x)
        'Q': 1   # sqrt(x)
    }
    sample_independent_list = [{'a': 1}]
    # sample_independent_list = [{'a': 5.7695},
    #                            {'a': -4.1206},
    #                            {'a': 4.652},
    #                            {'a': -5.6193},
    #                            {'a': -3.2971},
    #                            {'a': -0.0599},
    #                            {'a': 1.1835},
    #                            {'a': -8.2814},
    #                            {'a': 4.4342},
    #                            {'a': 4.1843}]
    #
    # sample_dependent_variable = [232.107, -56.1063, 127.968, -150.481, -27.2686,
    #                              0.943473, 5.24187, -506.651, 112.282, 95.9529]
