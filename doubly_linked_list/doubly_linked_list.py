"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

# allows you to add a node after the chosen node
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

# allows you to add a node BEFORE the chosen node
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

# delete chosen node
    def delete(self):
        # gives previous node pointer to its new next
        if self.prev:
            self.prev.next = self.next
        # gives the next node the pointer to its new previous
        if self.next:
            self.next.prev = self.prev


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

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)

        # beofre adding head, is there a head to replace, or a new list is being made
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # moves current head to be second, and new node is now head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # check to see if list is empty
        if self.head is None:
            return None
        # check to see if list is 1 long
        elif self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        # list is more than 1 long
        else:
            old_head = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
# check length of list to see if new
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # list isnt empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # check length of list is more than the 1 node
        if self.length > 1:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail.prev = None
            self.tail = new_tail
            self.length -= 1
            return old_tail.value
        # in case there is 1 node
        elif self.length == 1:
            old_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return old_tail.value
        # so you can try and delete node from an empty list
        else:
            return None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # delete node
        self.delete(node)
        # clone node in head spot
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        self.delete(node)
        # clone to tail
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # check if list is 1 long
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        # check if head
        elif node == self.head:
            self.remove_from_head()
        # check if tail
        elif node == self.tail:
            self.remove_from_tail()
        # free to delete
        else:
            next_node = node.next
            prev_node = node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # make sure list isnt 0
        if self.length > 0:
            max_value = self.head.value
            current = self.head
            # loop thru list comparing values and seting max to new max when current is bigger
            while current.next != None:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            if max_value > current.value:
                max_value = max_value
            else:
                max_value = current.value

            return max_value
        # if list is 0 there is no max
        else:
            return None
