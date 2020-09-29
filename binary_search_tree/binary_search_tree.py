"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class Node:
    def __init__(self, value=None, next_node=None):
        # what attributes do we need?
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # creat a new Node
        new_node = Node(value)
        if self.head is None:
          # updat head & tail attributes
            self.head = new_node
            self.tail - new_node
        else:
           # set the next node of my new Node to the head
            new_node.set_next_node(self.head)
        # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # consider two cases # the LL is empty
        if self.head is None:
          # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is Not empty
        else:
            # update next_node of out tail
            self.tail.set_next_node(new_node)
        # update self.tail
            self.tail = new_node

    def remove_head(self):
        # cases to consider?
        # empy list
        if self.head is None:
            return None
        # else, return Value of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):

        # TODO
        # when removing from the tail

        # empy list?
        if self.head is None:
            return None
            # else return value of old head
        else:
            ret_value = self.tail.get_value()

        # list with 1 elements?
            if self.head == self.tail:
                self.head = None
                self.tail = None
        # list with +2 elements?
            else:
                # if curren. next node is not the tail
                # asign current to current.next. then you set it to NONE making it the new tail.
                # return the current value after
                current = self.head
                while current.next_node is not self.tail:
                    current = current.next_node
                #
                current.set_next_node(None)
                self.tail = current

            return ret_value

    def contains(self, value):
        # TODO time permitting
        # loop through LL unitl the next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
        # return True
        return False
        #  return False

    def get_max(self):
        # TODO time permitting
        pass


class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        '''lsize = self.size
        array = self.storage
        # while array is None:
        if not array:
            return len(array)
        array = lsize
        return len(array)'''
        # return len(self.storage)
        return self.size

    def enqueue(self, value):
        # newstorage = self.storage
        # newstorage.insert(0, value)

        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
        return self.storage.remove_head()

        # if len(self.storage) == 0:
        # return None
        # else:

        # return self.storage.pop()


class Node:
    def __init__(self, value=None, next_node=None):
        # what attributes do we need?
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # creat a new Node
        new_node = Node(value)
        if self.head is None:
          # updat head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
           # set the next node of my new Node to the head
            new_node.set_next_node(self.head)
        # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # consider two cases # the LL is empty
        if self.head is None:
          # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is Not empty
        else:
            # update next_node of out tail
            self.tail.set_next_node(new_node)
        # update self.tail
            self.tail = new_node

    def remove_head(self):
        # cases to consider?
        # empy list
        if self.head is None:
            return None
        # else, return Value of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):

        # TODO
        # when removing from the tail

        # empy list?
        if self.head is None:
            return None
            # else return value of old head
        else:
            ret_value = self.tail.get_value()

        # list with 1 elements?
            if self.head == self.tail:
                self.head = None
                self.tail = None
        # list with +2 elements?
            else:
                # if curren. next node is not the tail
                # asign current to current.next. then you set it to NONE making it the new tail.
                # return the current value after
                current = self.head
                while current.next_node is not self.tail:
                    current = current.next_node
                #
                current.set_next_node(None)
                self.tail = current

            return ret_value

    def contains(self, value):
        # TODO time permitting
        # loop through LL unitl the next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
        # return True
        return False
        #  return False

    def get_max(self):
        # TODO time permitting
        pass


class Stack:
    def __init__(self):
        # Learn how to set a uderlying sorage structure.
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # array = self.storage
        # if array == []:
        # return
        # else:
        # return len(array)
        # return len(self.storage)
        return self.size

    def push(self, value):
        # return self.storage.append(value)
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
        return self.storage.remove_head()
        # if len(self.storage) == 0:
        # return None
        # else:
        # return self.storage.pop()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see that there is no left child, then we can wrap the
            # value i a BSTNode and park it
            if self.left is None:
                # otherwise there is a child
                self.left = BSTNode(value)
            else:
                # call the left child's `insert` method
                self.left.insert(value)
             # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see there is no right child, then we can wrap the
            if self.right is None:
                # value in a BSTNode and park it
                self.right = BSTNode(value)
        # otherwise there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return self.value

    def get_max(self):
        current = self

        while(current.right):
            if current is None:
                return
            current = current.right

        return current.value

        # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left is None and self.right is None:
            return
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # left, root, right
        # RECURSIVE - place your print statement in between recursive

        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        # create a Queue to keep track of nodes we are processing
        # add `self` to front of the queue
        queue = Queue()
        queue.enqueue(self)
        # while something still in the queue

        while len(queue) > 0:
            current = queue.dequeue()
            # call `print()`
            print(current.value)
            # enqueue  its left and right children
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        # create a STACK to keep track of nodes we are processing

        # push `self` into stack

        # while something still in the stack
        stack = [self]
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

        # (not processing all nodes)
        # pop the node off the top of the stack
        # call `print()`
        # push its left and right children into the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self):
        # root, left, right
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # left, right, root
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
