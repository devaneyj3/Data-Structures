class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next if next is not None else None
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            
    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return
            
        current = self.head
        
        while current.get_next() is not self.tail:
            current = current.get_next()
        
        val = self.tail.get_value()
        self.tail = current
        return val
        
    def remove_head(self): 
        if not self.head:
            return 
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        
        val = self.head.get_value()
        self.head = self.head.get_next()
        return val
    
    def contains(self, value):
        if not self.head:
            return False
        
        current = self.head
        while current:
            
            if current.get_value() == value:
                return True
            
            current = current.get_next()
        return False
        

    def get_max(self):
        # We're going to grab the initial value, from the head of the *LinkedList*
        # This distinction is important because the LinkedList *is not aware of any of it's nodes*,
        # except for the head and tail.
        current = self.head 
        # We're going to grab the initial value, from the head of the *LinkedList*
        # This distinction is important because the LinkedList *is not aware of any of it's nodes*,
        # except for the head and tail.
        # from the `current` variable, meaning max value is equivalent to self.head.value.
        max_val = current
        # Next we check if the head is `None`, because if it is, the max value is None, unless
        # there's only one node, in which case the max is the singular node's value
        if self.head is None:
            return None
        else:
            # Next we check if the head is `None`, because if it is, the max value is None, unless
            # there's only one node, in which case the max is the singular node's value
            while current.next is not None: 
                # We immediately set current to current.next, because we have the value from current in `max_val`,
                # so, we want to go to our second node, to get a value to compare to the first.
                current = current.next 
                if current.value > max_val.value: 
                    # Now that we have two values, we can compare them, and if the current.value (which is equivalent to current.next.value),
                    # is greater than `max_val`,
                    max_val = current.value # then we set max_val to that value.
                    return max_val
            # if head doesn't have a node next to it,'
            max_val = self.head.value
            return max_val