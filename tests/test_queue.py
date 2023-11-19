import pytest
from src.queue import Node, Queue


@pytest.fixture
def node1():
    return Node('data1')


@pytest.fixture
def node2():
    return Node('data2')


@pytest.fixture
def node3():
    return Node('data3')


@pytest.fixture
def queue1():
    return Queue()


def test_node_init(node1, node2):
    assert node1.data == 'data1'
    assert node1.next_node == None
    assert node2.data == 'data2'
    assert node2.next_node == None


def test_queue_init(queue1):
    assert queue1.tail == None
    assert queue1.head == None


def test_queue_enqueue(queue1):
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')
    assert queue1.head.data == 'data1'
    assert queue1.head.next_node.data == 'data2'
    assert queue1.head.next_node.next_node.data == 'data3'
    assert queue1.tail.data == 'data3'
    assert queue1.tail.next_node is None
    with pytest.raises(AttributeError):
        assert queue1.tail.next_node.data == 0


def test_queue_str(queue1):
    assert str(queue1) == ""
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')
    assert str(queue1) == "data1\ndata2\ndata3"


def test_queue_dequeue(queue1):
    assert queue1.dequeue() == None
    queue1.enqueue('data1')
    assert queue1.dequeue() == 'data1'
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    assert queue1.dequeue() == 'data1'
    assert queue1.dequeue() == 'data2'
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')
    assert queue1.dequeue() == 'data1'
    assert queue1.head.data == 'data2'
    assert queue1.head.next_node.data == 'data3'
    assert queue1.tail.data == 'data3'
    assert queue1.dequeue() == 'data2'
    assert queue1.dequeue() == 'data3'
    assert queue1.dequeue() == None
