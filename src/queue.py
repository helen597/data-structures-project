class Node:
    """Класс для узла очереди"""


    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""


    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None


    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if isinstance(data, Node):
            self.tail = data
        else:
            new_node = Node(data, None)
            if self.tail:
                self.tail.next_node = new_node
            self.tail = new_node
            if not self.head:
                self.head = new_node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass


    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.tail:
            return ""
        str1 = self.head.data
        if self.head.next_node:
            new_node = self.head.next_node
            str1 += ('\n' + new_node.data)
        while new_node.next_node:
            new_node = new_node.next_node
            str1 += ('\n' + new_node.data)
        return str1
