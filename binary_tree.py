

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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

