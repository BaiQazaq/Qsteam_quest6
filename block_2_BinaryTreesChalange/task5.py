# 5 . Implement a method to find the maximum depth of a binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_depth(root):
    # Base case: if the node is None, the depth is 0
    if not root:
        return 0
    
    # Recursive case: calculate the depth of the left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the maximum depth of the current node
    return max(left_depth, right_depth) + 1

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Find the maximum depth of the tree
depth = max_depth(root)

# Print the result
print("Maximum Depth of the Binary Tree:", depth)
