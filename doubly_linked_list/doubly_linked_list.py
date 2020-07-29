"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
    def remove(self): 
        # print(f' self value is {self.value}')
        if self.prev:
            # print(f' self value is {self.value}')
            # print(f'Now self previos head is {self.prev.value}')
            self.prev.next = self.next
            self.next = None
        if self.next:
            # print(f' self value is {self.value}')
            # print(f'Now self next head is {self.next.value}')
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
    
    def __str__(self):
        print(f' {self.head.value}  {self.tail.value}')
        
    
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_head_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            # make head node
            # set new node to be head and tail
            self.head = new_head_node # 5
            self.tail = new_head_node
        else:   
            new_head_node.next = self.head 
            self.head.prev = new_head_node 
            
            new_head_node.prev = None
            
            self.head = new_head_node
            print(f'set head node: {self.head.value}')
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return
        if not self.head.next:
            self.length -= 1
            head = self.head
            self.head = None
            self.tail = None
            return head.value
        current = self.head.value
        print(current)
        self.head = self.head.next
        self.length -= 1
        
        return current
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
        if self.tail is None and self.head is None:
            # make head node
            # set new node to be head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # set previous of new node to the tail
            new_node.prev = self.tail
            self.tail.next = new_node
            
            self.tail = new_node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if we call move_to_front on head node set that node to head
        if node is self.head:
            return
        value = node.value
        # if node is self.tail
        if node is self.tail:
            self.remove_from_tail()
            self.add_to_head(value)
        else:
            node.remove()
            self.length -= 1
            self.add_to_head(value)
        
        
            # print(f'self.tail: {self.tail.value}')
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        print(value)
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
            print(f'self.tail: {self.tail.value}')
        else:
            node.remove()
            self.length -= 1
            self.add_to_tail(value)
            

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if there is no head or tail return none
        self.length -= 1
        if not self.head and not self.tail:
            return None
        # this part works
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            print(f'line 143 Now self head is {self.head.value}')
            self.head = node.next
            node.remove()
        elif self.tail == node:
            # print(f'self tail is {self.tail.value}')
            self.tail = node.prev
            node.remove()
        else:
            node.remove()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # there is no head so return
        if not self.head:
            return
        current = self.head
        maximum = self.head.value
        while current:
            if current.value > maximum: 
                maximum = current.value
            current = current.next
        return maximum
        
        
    
# value = DoublyLinkedList()
# value.add_to_head(1)
# value.add_to_tail(3)
# value.move_to_front(3)
# # # # value.delete(13)
# # print(value.__len__())
# value.__str__()
