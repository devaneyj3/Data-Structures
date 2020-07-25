"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next.value
    
    def set_next(self, new_next):
        self.next = new_next
    
    def get_previous(self):
        return self.prev
    
    def set_previous(self, prevNode):
        self.prev = prevNode
            
            
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
    
    def __str__(self):
        print(f'{self.head.value} -> {self.head.next.value} -> {self.tail.value}')
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_head_node = ListNode(value, None, None)
        self.length += 1
        if self.head is None:
            # make head node
            # set new node to be head and tail
            self.head = new_head_node # 5
            self.tail = new_head_node
        else:   
            new_head_node.next = self.head #5
            self.head.prev = new_head_node 
            
            self.head = new_head_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # print(f'{self.head.value} -> {self.tail.value}')
        # print(f'{self.tail.prev.value} -> {self.head.next.value}')
        if self.tail is None:
            # make head node
            # set new node to be head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # set previous of new node to the tail
            new_node.prev = self.tail
            self.tail.next = None
            
            self.tail = new_node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if no head exists node is in current spot
        if self.head is None:
            # node has to be the head
            self.head = node
        
        targetNode = None
        # find the node
        current = self.head
        print(f"Current head is {current.value}")
        print(f"Current.previous is {current.prev.value}")
        while current.prev is not None:
            current = current.prev
            if current == node:
                targetNode = current
                return targetNode
        print(f'target node is {targetNode}')
        # if there are current nodes move node to previous node until it is at the head
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
    
value = DoublyLinkedList()
# value.add_to_head(1)
# value.add_to_head(10)
# value.add_to_head(13)
# value.add_to_head(44)
value.add_to_tail(13)
value.add_to_tail(16)
# value.__str__()
