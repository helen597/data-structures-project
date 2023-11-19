"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack


@pytest.fixture
def node1():
    return Node(5, None)


@pytest.fixture
def node2(node1):
    return Node('a', node1)


@pytest.fixture
def node3():
    return Node('data3')


@pytest.fixture
def stack1():
    return Stack()


def test_node_init(node1, node2):
    assert node1.data == 5
    assert node1.next_node == None
    assert node2.data == 'a'
    assert node2.next_node == node1


def test_stack_init(stack1):
    assert stack1.top == None


def test_stack_push(stack1, node1, node2):
    assert stack1.top == None
    stack1.push(node1)
    assert stack1.top == node1
    stack1.push(node2)
    assert stack1.top == node2

def test_stack_pop(stack1,node1,node2):
    assert stack1.pop() == None
    stack1.push('data1')
    data = stack1.pop()
    assert stack1.top is None
    assert data == 'data1'
    # assert stack1 == []
    stack1.push('data1')
    stack1.push('data2')
    data = stack1.pop()
    assert stack1.top.data == 'data1'
    assert data == 'data2'
    stack1.push(node1)
    stack1.push(node2)
    data = stack1.pop()
    assert stack1.top.data == 5
    assert data == 'a'


def test_stack_str(stack1, node1, node2, node3):
    assert str(stack1) == ''
    stack1.push(node1)
    assert str(stack1) == 'Стэк:\n5'
    stack1.push(node2)
    assert str(stack1) == 'Стэк:\na\n5'
    stack1.push(node3)
    assert str(stack1) == 'Стэк:\ndata3\na\n5'
