# 1. Write a program to check if a binary tree is balanced.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

    def is_balanced_helper(node):
        if node is None:
            return True

        left_height = height(node.left)
        right_height = height(node.right)

        # Check if the subtree is balanced for the current node
        if abs(left_height - right_height) > 1:
            return False

        # Check recursively for left and right subtrees
        return is_balanced_helper(node.left) and is_balanced_helper(node.right)

    return is_balanced_helper(root)

# Example usage
if __name__ == "__main__":
    # Creating a balanced binary tree
    balanced_tree_root = TreeNode(1)
    balanced_tree_root.left = TreeNode(2)
    balanced_tree_root.right = TreeNode(3)
    balanced_tree_root.left.left = TreeNode(4)
    balanced_tree_root.left.right = TreeNode(5)

    # Creating an unbalanced binary tree
    unbalanced_tree_root = TreeNode(1)
    unbalanced_tree_root.left = TreeNode(2)
    unbalanced_tree_root.right = TreeNode(3)
    unbalanced_tree_root.left.left = TreeNode(4)
    unbalanced_tree_root.left.left.left = TreeNode(5)

    # Checking if the trees are balanced
    print("Is the balanced tree balanced?", is_balanced(balanced_tree_root))
    print("Is the unbalanced tree balanced?", is_balanced(unbalanced_tree_root))
