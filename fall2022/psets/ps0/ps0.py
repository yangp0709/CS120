#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Checks whether or not there exists a vertex
    if v is None:
        return 0

    # Calculates the sizes of the left and right children adding the one vertex
    else:
        v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
        return v.size
    pass

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 

    #Check if vertex exists
    if r is None:
        return 0

    a = r 
    n = r.size/2

    #Check if the left and right children exist
    if a.left is None and a.right is not None:
        return a.right
    #Check if the left or right children is larger
    elif a.right is None and a.left is not None:
        return a.left
    
    elif a.right is None and a.left is None:
        return a
    
    #Look at the edge cases
    if a.right is None and a.left is None:
        parent= r.size - a.size

        if parent.size < n and a.size < n:
            return a
    
    if a.left.size and a.right.size < n:
        return a
    #If there's children then recursively go through the children that is larger
    elif a.left.size > a.right.size:
        find_vertex(a.left)
    elif a.left.size < a.right.size:
        find_vertex(a.right)
    pass