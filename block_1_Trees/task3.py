# 10. Implement a binary tree and perform a level-order traversal.

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.key)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    tree_root = TreeNode(1)
    tree_root.left = TreeNode(2)
    tree_root.right = TreeNode(3)
    tree_root.left.left = TreeNode(4)
    tree_root.left.right = TreeNode(5)
    tree_root.right.left = TreeNode(6)
    tree_root.right.right = TreeNode(7)

    # Performing level-order traversal
    result = level_order_traversal(tree_root)

    print("Level-order Traversal:")
    print(result)
