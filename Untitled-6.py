class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    # If tree is empty, create a new node
    if root is None:
        return Node(key)

    # Insert into left subtree
    if key < root.key:
        root.left = insert(root.left, key)

    # Insert into right subtree
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Create an empty BST
root = None

# Insert elements
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

# Display BST using inorder traversal
print("Inorder Traversal:")
inorder(root)