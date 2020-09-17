# TODO a class that represents the individual elements in our LL
class Node:
    def __init__(self, value=None, next_node=None):
        # what attributes do we need?
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self, new_next):
        self.next_note = new_next


class LinkedList:

    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
             # creat a new Node
           new_node = Node(-1)
    if self.head is None:
          # updat head & tail attributes

           self.head = new_node
           self.tail - new_node

    elif self.head == self.tail:

        # TODO time permitting
        # ceate a new Node
        new_node = Node(-1)
        # set the next node of my new Node to the head
        new_node.set_next_node(self.head)
        # update the head attribute
        self.head = new_node

    def add_to_tail(self, value):
        # TODO
        # create a new Node
        new_node = Node(value)
        # consider two cases # the LL is empty
       if self.head is None:
          # update head & tail attributes
          self.head = new_node
          self.head = new_node
        # 2. LL is Not empty 
       else:
        # update next_node of out tail
        self.tail.set_next_node(n)
        # update self.tail 





    def remove_head(self):
        # TODO  
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
            self.head = self.head.get_head_next_node()
        return ret_value 

     def remove_tail(self):
      # TODO
      # empy list? 
      # list with 1 elements?
      # list with +2 elements?

     def contains(self, value):
        # TODO time permitting
        # loop through LL unitl the next pointer is None
        cur_node = self.head
        while cur_done is not None:
        # if we find 'value'
        if cur_node.get_value() == value :
            return True
        # return True 
        return False
        #  return False 

     def get_max(self):
        # TODO time permitting
