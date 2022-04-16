
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    
    def __repr__(self):
        return f'{self.key}'


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is not None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)


def min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current


def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        print("root key:", root.key)
        if root.left is None:
            print("left is empty")
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            print("right is empty")
            temp = root.left
            root = None
            return temp
        print("nested else")
        temp = min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)
print("\nmin value:", min_value(root).key)
print("\nmax value:", max_value(root).key)

deleted_node = delete(root,6)
print("deleted node:", deleted_node.key)
inorder(root)

"""

Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.


"""



def create_min_bst(arr):
    return create_min_height(arr, 0, len(arr)-1)


def create_min_height(arr, start, end):
    if end<start:
        return None
    
    middle = (start+end)//2
    node = Node(arr[middle])
    node.left = create_min_height(arr, start, middle-1)
    node.right = create_min_height(arr, middle+1, end)
    return inorder(node)




create_min_bst([4,5,6,7,8,9,10])




"""

List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).


"""



def create_level_linked_list(root):
    depth_lists =[]
    depth = 0
    specfiy_depth(root,depth_lists,depth)
    return depth_lists



def specfiy_depth(root,depth_lists,depth):

    if root is None:
        return None
    
    current_level_nodes = []

    if len(depth_lists) == depth:
        current_level_nodes = []
        depth_lists.append(current_level_nodes)
    else:
        current_level_nodes = depth_lists[depth]
    
    current_level_nodes.append(root)
    specfiy_depth(root.left,depth_lists,depth+1)
    specfiy_depth(root.right,depth_lists,depth+1)


root = None
root = insert(root, 41)
root = insert(root, 20)
root = insert(root, 29)
root = insert(root, 32)
root = insert(root, 11)
root = insert(root, 65)
root = insert(root, 50)
root = insert(root, 91)
root = insert(root, 72)
root = insert(root, 99)

print("\nInorder traversal: ", end=' ')
inorder(root)


print(create_level_linked_list(root))