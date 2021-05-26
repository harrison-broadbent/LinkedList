import pytest
from LinkedList import LinkedList


class TestLinkedList:
    def test_initialization(self):
        ll = LinkedList()
        assert ll.head is None

    def test_add_and_get_first(self):
        ll = LinkedList()
        ll.addFirst(0)
        assert ll.getFirst() == 0

    def test_add_and_get_last(self):
        ll = LinkedList()
        ll.addLast(0)
        assert ll.getLast() == 0

    def test_showList(self, capsys):
        ll = LinkedList()
        ll.addLast(0)
        ll.addLast(1)
        ll.addLast(2)

        ll.showList()
        captured = capsys.readouterr()

        assert captured.out == "0->1->2\n"

    def test_reverse(self, capsys):
        ll = LinkedList()
        ll.addLast(1)
        ll.addLast(2)
        ll.addLast(3)

        # ll                    =   1->2->3
        # ll.reverse() becomes      3->2->1
        ll.reverse()
        ll.showList()
        captured = capsys.readouterr()

        assert captured.out == "3->2->1\n"

    def test_nodes_must_be_integers(self):
        with pytest.raises(ValueError):
            ll = LinkedList()
            ll.addLast("raises an error")

    def test_remove_last_when_empty_raises_error(self):
        with pytest.raises(IndexError):
            ll = LinkedList()
            ll.removeLast()

    def test_remove_first_when_empty_raises_error(self):
        with pytest.raises(IndexError):
            ll = LinkedList()
            ll.removeFirst()
