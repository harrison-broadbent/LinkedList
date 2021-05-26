###################################################################
# Harrison Broadbent                                              #
# StartMate Student Fellowship submission - Backend Engineering   #
# Github - https://github.com/harrison-broadbent/LinkedList       #
# Replit - https://replit.com/join/emszlrgk-harrisonbroadbent     #
#                                                                 #
# Task: Create a LinkedList                                       #
###################################################################


# Node (int data) -
#   self.data: int
#   self.next: Node
#
# Basic Node class for the LinkedList.
# LinkedList is composed of Node instances strung together.
class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None

    def __repr__(self):
        return "Data: " + str(self.data) + ", Next: " + str(self.next)


# LinkedList() -
#   self.head: Node
#
#   - addFirst(int e) : adds an element e to the front of the list.
#   - addLast(int e)  : adds an element e to the end of the list.
#   - removeLast()    : removes the last element of the list and returns it.
#   - removeFirst()   : removes the first element of the list and returns it.
#   - getFirst()      : returns the value of the first element in the list.
#   - getLast()       : returns the value of the last element in the list.
#   - reverse()       : reverses the LinkedList.
#   - showList()      : prints the list out.
#
#
# LinkedList class representing a chain of Nodes.
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return "->".join(nodes)

    # addFirst(int e): Create a Node with data = e,
    # and add it to the front of the LinkedList.
    # Runtime: O(1)
    #
    # INPUT: (int) element to add.
    # OUTPUT: void
    def addFirst(self, e):
        new_node = Node(e)
        new_node.next = self.head

        self.head = new_node

    # addLast(int e): Create a Node with data = e,
    # and add it to the end of the LinkedList.
    # Runtime: O(n)
    #
    # INPUT: (int) e to add.
    # OUTPUT: void
    def addLast(self, e):

        if self.head is None:
            self.head = Node(e)

        else:
            header_pointer = self.head
            while header_pointer.next is not None:
                header_pointer = header_pointer.next

            header_pointer.next = Node(e)

    # removeLast(): removes the last Node from the LinkedList,
    # returning the removed Node.
    # Runtime: O(n)
    #
    # INPUT: void
    # OUTPUT: (int) element removed.
    def removeLast(self):
        if self.head is None:
            raise IndexError("No elements exist in the list.")

        if self.head.next is None:
            removed_element = self.head.data
            self.head = None
            return removed_element

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next

        removed_element = second_last.next.data
        second_last.next = None
        return removed_element

    # removeFirst(): removes the first Node of the LinkedList,
    # returning the removed Node.
    # Runtime: O(1)
    #
    # INPUT: void
    # OUTPUT: (int) element removed.
    def removeFirst(self):
        if self.head:
            removed_element = self.head.data
            self.head = self.head.next
            return removed_element
        else:
            raise IndexError("No elements exist in the list.")

    # getFirst(): returns the first Node value of the LinkedList.
    # Runtime: O(1)
    #
    # INPUT: void
    # OUTPUT: (int) first element of list.
    def getFirst(self):
        if self.head:
            return self.head.data
        else:
            return None

    # getLast(): returns the last Node value of the LinkedList.
    # Runtime: O(n)
    #
    # INPUT: void
    # OUTPUT: (int) last element of list.
    def getLast(self):
        if self.head:
            header_pointer = self.head
            while header_pointer.next is not None:
                header_pointer = header_pointer.next
            return header_pointer.data
        else:
            return None

    # reverse(): reverses the LinkedList, mutating the existing list.
    # Runtime: O(n^2)
    #
    # INPUT: void
    # OUTPUT: void
    def reverse(self):
        if self.head:
            # reversed_list points to the head of the reversed list.
            reversed_list = Node(self.removeLast())

            # reversed_list_ptr points to the final node of the reversed list.
            reversed_list_header = reversed_list
            while self.getLast() is not None:
                reversed_list.next = Node(self.removeLast())
                reversed_list = reversed_list.next

            self.head = reversed_list_header

        else:
            return None

    # showList(): prints the LinkedList.
    # Runtime: O(n)
    #
    # INPUT: void
    # OUTPUT: void (print list)
    def showList(self):
        print(self)


"""

from LinkedList import *

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n0 = Node(0)

ll = LinkedList()
ll.head = n1

n1.next = n2
n2.next = n3

ll

"""
