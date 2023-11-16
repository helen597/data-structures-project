class Node:
    """Класс для узла стека"""


    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""


    def __init__(self):
        """Конструктор класса Stack"""
        # self.stack = []
        self.top = None


    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if isinstance(data, Node):
            self.top = data
        else:
            new_node = Node(data, self.top)
            self.top = new_node


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top:
            popped_data = self.top.data
            self.top = self.top.next_node
            return popped_data
        else:
            return None


    def __str__(self):
        if self.top:
            return f"{self.top.data}"
        return ""
