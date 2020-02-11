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
