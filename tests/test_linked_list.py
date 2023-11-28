"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest
from src.linked_list import LinkedList, Node


@pytest.fixture
def node1():
    return Node({'id': 1})


def test_node_init(node1):
    assert Node({'id': 1}).data == {'id': 1}
    assert node1.next_node == None


def test_linked_list():
    ll = LinkedList()
    assert str(ll) == 'None'
    ll.insert_beginning({'id': 1})
    assert ll.head.data == {'id': 1}
    assert ll.tail.data == {'id': 1}
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
    ll = LinkedList()
    ll.insert_at_end({'id': 1})
    assert ll.head.data == {'id': 1}
    assert ll.tail.data == {'id': 1}
