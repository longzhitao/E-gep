# This Python file uses the following encoding: utf-8
from collections import deque
from setting import Parameter
priority = Parameter.priority


def priority_level(operator1, operator2):
    if (operator1 in priority) and (operator2 in priority):
        if priority[operator1] >= priority[operator2]:
            return 1
        else:
            return 0
    else:
        return 0


class Node(object):
    def __init__(self, var):
        self.var = var
        self.l_child = None
        self.r_child = None
        pass


class ExpressionTree(object):
    __slots__ = ['expression', 'root', 'infix_expression', 'valid']

    def __init__(self, expression: list):
        self.expression = expression
        self.root = Node(expression[0])
        self.infix_expression = list()
        self.valid = 0
        pass

    def create(self):
        index = 0
        queue = deque()
        queue.append(self.root)

        while True:
            # print(len(queue))
            for i in range(len(queue)):
                node = queue.popleft()

                if node.var in Parameter.operand and index != len(self.expression) - 1:
                    if Parameter.operand.get(node.var) == 2:
                        index += 1
                        node.l_child = Node(self.expression[index])
                        queue.append(node.l_child)

                        index += 1
                        node.r_child = Node(self.expression[index])
                        queue.append(node.r_child)

                    else:
                        index += 1
                        node.r_child = Node(self.expression[index])
                        queue.append(node.r_child)

            if len(queue) == 0:
                break

        self.valid = index
        self.in_order_traversal(self.root)
        self.infix_expression.insert(0, '(')
        self.infix_expression.insert(len(self.infix_expression), ')')
        pass

    def in_order_traversal(self, node):
        if node is not None:
            if node.l_child is not None:
                temp = priority_level(node.var, node.l_child.var)
                if temp == 1:
                    self.infix_expression.append('(')

                self.in_order_traversal(node.l_child)

                if temp == 1:
                    self.infix_expression.append(')')

            self.infix_expression.append(node.var)

            if node.r_child is not None:
                temp = priority_level(node.var, node.r_child.var)
                if temp == 1:
                    self.infix_expression.append('(')

                self.in_order_traversal(node.r_child)
                if temp == 1:
                    self.infix_expression.append(')')
        pass
