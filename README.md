# E-gep

基因表达式编程（Gene Expression Programming），默认测试数据为太阳黑子

![image](https://github.com/longzhitao/E-gep/blob/master/images/matplotlib.jpg)

参数配置在setting.py下，其中主要参数如下

    ```python
    
    function_set = list('+-*/')  # 函数集
    terminal_set = list('abcdefghij')  # 终点集
    # func_ter_set = list('+-*/a')
    head_length = 7  # 头长度
    tail_length = 8  # 尾长度
    gene_length = 15  # 基因长度 = 头长度 + 尾长度

    connection = ['+']  # 连接符
    num_of_genes = 3    # 单条染色体基因个数

    mutation_rate = 0.044   # 变异率
    one_point_recombination_rate = 0.3  # 单点重组率
    two_point_recombination_rate = 0.3  # 双点重组率
    gene_recombination_rate = 0.1   # 基因重组率
    IS_transposition_rate = 0.1     # IS转座率
    RIS_transposition_rate = 0.1    # RIS转座率
    gene_transposition_rate = 0.1   # 基因转座率

    IS_elements_length = 3          # IS转座长度
    RIS_elements_length = 3         # RIS转座长度

    max_fitness = 1000              # 最大适应度值
    ```
