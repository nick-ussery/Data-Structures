# lists store things in sequential order
# allow us to index to fetch by particular index


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # needs to have a node to add the list to
        new_node = Node(value)
        # check if Linked List is empty
        if self.head is None and self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # update the last node's next_node property to the new node
            self.tail.set_next(new_node)
            # update the self.tail to point the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only 1 node
        elif self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        # otherwise the linked list has more than 1 node
        else:
            # set self.tail to be previous node(second to last node)
            # store the last Node's value in another variable so we can return it
            val = self.tail.get_value()
            # only way to point at the second to last node is to traverse the whole linked lsit from the beginning
            # init aothe reference to keep track of where we are in the linked list as we iterate
            current = self.head
            # keep iterating until current == tail
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()
            # after loop, new tail is found
            self.tail = current
            # set new tail's next_node to None
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # store the old head's value to return
        # set the self.head to the next_node of the old head
        # then return old heads value
        # usual checks: linked list is empty
        if self.head is None and self.tail is None:
            return None

        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val
