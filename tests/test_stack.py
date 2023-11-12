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


def stack1():
    return Stack()


def test_node_init(node1, node2):
    assert node1.data == 5
    assert node1.next_node == None
    assert node2.data == 'a'
    assert node2.next_node == node1


def test_stack_init(stack1):
    assert stack1.stack == []


def test_stack_push(stack1, node1, node2):
    stack1.push(node1)
    stack1.push(node2)
    # assert stack1 == None
