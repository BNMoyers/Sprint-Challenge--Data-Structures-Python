class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare new value to current value, move left or right accordingly. 
        #if moving left, repeat until target is higher than all available values; the value goes here.
        #if moving right, do the opposite
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #compare target to value
        #check if the target is smaller or greater than the root
        #if smaller, go left, if larger go right.
        #repeat until we find the value or until we hit leaves
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
            
    # Return the maximum value found in the tree
    def get_max(self):
        #go down right side as far as possible
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #call the function on the root
        #check the left to see if it's empty; if not, call the function; repeat
        #repeat same down right side
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)