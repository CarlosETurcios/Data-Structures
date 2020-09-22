"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None, ):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self,):
        self.prev = None
        self.next = None


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def debug(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create new_node
        new_node = ListNode(value)
        # 1. add to empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            # 2 add to nonempty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            # update length
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self, ):
        current = self.head

        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return current.value

        else:
            nxt = current.next
            nxt.prev = None
            current.next = None
            self.head = nxt
            self.length -= 1
            return current.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)
        current_tail = self.tail
        # add to empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            current_tail.next = new_node
            new_node.prev = current_tail
            self.tail = new_node
            # update length
            self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        current = self.tail
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
        else:
            prev = current.prev
            prev.next = None
            current.prev = None
            self.tail = prev
            self.length -= 1
            return current.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return None
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return None
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        # dont need to return value
        # DO need to update head, tail
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif node is self.head:  # list had +2 nodes
            print('howdy')
            self.head = node.next
            node.delete()  # updating prev and/or next pointers
            self.head.prev = None
            self.length -= 1
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
            self.tail.next = None
            self.length -= 1
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.delete()

            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        current = self.head
        maxNumber = self.head.value

        while current.next is not None:

            if maxNumber < current.next.value:
                maxNumber = current.next.value

            current = current.next
        return maxNumber
