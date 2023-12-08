# 4. Implement a pre-order traversal in a binary tree.
# 5. Write a method for post-order traversal in a binary tree.



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")  # Visit the current node
            self.preorder_traversal(node.left)  # Traverse the left subtree
            self.preorder_traversal(node.right)  # Traverse the right subtree

    def postorder_traversal(self, node):
        
        if node:
            self.postorder_traversal(node.left)  # Traverse the left subtree
            self.postorder_traversal(node.right)  # Traverse the right subtree
            print(node.value, end=" ")  # Visit the current node

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    binary_tree = BinaryTree(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)
    binary_tree.root.left.left = Node(4)
    binary_tree.root.left.right = Node(5)

    # Performing pre-order traversal
    print("Pre-order Traversal:")
    binary_tree.preorder_traversal(binary_tree.root)

    print("Post-order Traversal:")
    binary_tree.postorder_traversal(binary_tree.root)
