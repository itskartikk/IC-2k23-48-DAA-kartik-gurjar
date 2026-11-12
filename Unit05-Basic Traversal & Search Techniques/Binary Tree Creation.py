
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    data = int(input("Enter node value (-1 for no node): "))

    if data == -1:
        return None

    root = Node(data)

    print(f"Enter left child of {data}:")
    root.left = create_tree()

    print(f"Enter right child of {data}:")
    root.right = create_tree()

    return root


def display_tree(root):
    if root is None:
        return

    print(root.data, end=" ")
    display_tree(root.left)
    display_tree(root.right)


root = create_tree()

print("Binary Tree (Preorder):")
display_tree(root)
