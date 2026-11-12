
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Postorder Traversal:")
postorder(root)
