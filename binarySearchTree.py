"""
A binary search tree is a binary tree with keys stored in the nodes
which satisfy the following property (binary-search-tree-property).
If y and z are nodes in left subtree and right subtree, respectively,
of node x, then key(x) >= key(y) and key(x) <= key(z)
"""
#it is a pseudo code

#O(h), h is height of the tree
def FindMax(x):
    while (x.right != NULL):
        x = x.right
    return x

#O(h), h is the height of the tree
def FindMin(x):
    while (x.left != NULL):
        x = x.left
    return x

#O(h), h is the height of the tree: using recursion
def search(x, k):
    if x == k or x == NULL:
        return x
    else:
        if k > x:
            search(x.right, k)
        elif k < x:
            search(x.left, k)

#O(h), h is the height of the tree: without using recursion
def search(x, k):
    while x != k or x != NULL:
        if k > x:
            x = x.right
        elif k < x:
            x = x.left
    return x

#O(h), h is the height of the tree
def successor(x):
    if x.right != NULL:
        x = x.right
        FindMin(x)
    else:
        y = parent(x)
        while y != NULL and x == y.right: #when y is not the root, and x is bigger than y
            x = y
            y = parent(y)
        return y
    
#O(h), h is the height of the tree
def predecessor(x):
    if x.left != NULL:
        x = x.left
        FindMax(x)
    else:
        y = parent(x)
        while y != NULL and x == y.left: #when y is not the root, and y is bigger than x
            x = y
            y = parent(y)
        return y