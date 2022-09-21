from re import A


class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1) #Take away what is already selected from the left and minus the root node
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1 #Add one to the side that a node is added instead of calculating the entire tree 
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1 #Add one to the side that a node is added instead of calculating the entire tree 
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 

    The implementation of rotate to size-agumented BSTs was no different than the algorithm we used and defined in class.
    It has runtime of O(1) because only one step pointers were used and one step computations were used for size. 
    The new rotation operation preserves the invariant of correct size-agumentations in that when we rotate left y size replaces x 
    size and x size is just the size of its two children plus itself as shown in Figure 11.2. This is similar for rotate right where
    y size becomes what x size used to be and x size is just the the size of its two children plus itself as shown in Figure 11.3.
    '''
    
    def rotate(self, direction, child_side):

        if direction == "L" and child_side == "R":
            a = self.right
            self.right = a.right
            a.right = self.right.left
            self.right.left = a
            self.right.size = a.size
            a.size = 1 + (a.right.size if a.right else 0) + (a.left.size if a.left else 0)


        if direction == "L" and child_side == "L":
            a = self.left
            self.left = a.right
            a.right = self.left.left
            self.left.left = a
            self.left.size = a.size
            a.size = 1 + (a.right.size if a.right else 0) + (a.left.size if a.left else 0)

        if direction == "R" and child_side == "L":
            a = self.left
            self.left = a.left
            a.left = self.left.right
            self.left.right = a
            self.left.size = a.size
            a.size = 1 + (a.right.size if a.right else 0) + (a.left.size if a.left else 0)


        if direction == "R" and child_side == "R":
            a = self.right
            self.right = a.left
            a.left = self.right.right
            self.right.right = a
            self.right.size = a.size
            a.size = 1 + (a.right.size if a.right else 0) + (a.left.size if a.left else 0)

        
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self