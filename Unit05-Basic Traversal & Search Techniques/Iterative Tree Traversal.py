
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Iterative Preorder: Root, Left, Right
def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


# Iterative Inorder: Left, Root, Right
def inorder(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


# Iterative Postorder: Left, Right, Root
def postorder(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().data, end=" ")


# Creating Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Iterative Preorder:")
preorder(root)

print("\nIterative Inorder:")
inorder(root)

print("\nIterative Postorder:")
postorder(root)
