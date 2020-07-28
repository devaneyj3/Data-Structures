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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # go to right
        if value <  self.value:
            # if nothing right insert
            if not self.left:
                self.left = BSTNode(value)
            else:
                # or repeat the process at the other parent nod
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)    
        # handle duplicates
        else:
            self.right = BSTNode(value) 
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is value 
        print(f'the target is {target}')
        if self.value == target:
            print('true')
            return True
        print(f'self.valus is {self.value}')
        # we go right if we do not find the value
        if self.value > target:
            print(f'target {target} is less than {self.value}')
            if self.left is not None:
                return self.left.contains(target)
        elif self.value < target:
            print(f'target {target} is greater than {self.value}')
            if self.right is not None:
                print(f'target {target} is going right')
                return self.right.contains(target)
        else: 
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # start with root node and assign that to value
        curr = self
        if not self.right:
            return curr.value
        # cycle through list to see the highest value
        while curr.right:
            curr = curr.right
        return curr.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # check for values on right and left
        if self.right:
            print(self.value)
        if self.left:
            print(self.left)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(5)

# bst.insert(8)
# bst.insert(5)
bst.insert(30)
# bst.insert(6)
bst.insert(300)
# bst.insert(4)
bst.insert(3)
# bst.contains(2)

bst.get_max()
# bst.in_order_print()
# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
