from linked_list import LinkedList


def test_init():
    linked_list = LinkedList(4)

    assert linked_list.head.value == 4
    assert linked_list.tail.value == 4


def test_append():
    linked_list = LinkedList(4)
    assert linked_list.length == 1

    linked_list.append(3)

    assert linked_list.length == 2
    assert linked_list.head.value == 4
    assert linked_list.head.next.value == 3
    assert linked_list.tail.value == 3

    linked_list.append(5)

    assert linked_list.length == 3
    assert linked_list.head.value == 4
    assert linked_list.head.next.next.value == 5
    assert linked_list.tail.value == 5


def test_pop():
    linked_list = LinkedList(4)
    popped = linked_list.pop()
    assert popped.value == 4

    linked_list.append(4)
    linked_list.append(3)

    popped = linked_list.pop()
    assert popped.value == 3

    linked_list = LinkedList(4)
    popped = linked_list.pop()

    assert popped.value == 4
    assert linked_list.length == 0

    linked_list.append(5)
    linked_list.append(4)

    popped = linked_list.pop()
    assert popped.value == 4
    assert linked_list.length == 1

    linked_list.append(3)
    linked_list.append(2)

    popped = linked_list.pop()
    assert popped.value == 2
    assert linked_list.length == 2


def test_prepend():
    linked_list = LinkedList(4)
    linked_list.prepend(3)

    assert linked_list.head.value == 3
    assert linked_list.head.next.value == 4
    assert linked_list.tail.value == 4

    linked_list.pop()
    linked_list.pop()
    linked_list.prepend(3)

    assert linked_list.head.value == 3
    assert linked_list.tail.value == 3


def test_pop_first():
    linked_list = LinkedList(4)
    popped = linked_list.pop_first()

    assert popped.value == 4

    popped = linked_list.pop_first()
    assert popped == None

    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    popped = linked_list.pop_first()
    assert popped.value == 3
    assert linked_list.length == 2


def test_get():
    linked_list = LinkedList(4)
    element = linked_list.get(3)
    assert element == None

    element = linked_list.get(-1)
    assert element == None

    element = linked_list.get(0)
    assert element.value == 4

    linked_list.prepend(3)
    element = linked_list.get(1)
    assert element.value == 4


def test_set():
    linked_list = LinkedList(4)
    linked_list.set(0, 5)
    assert linked_list.get(0).value == 5
