# 4. Write a program to check if two binary trees are identical.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_identical_trees(root1, root2):
    # Base cases: if both nodes are None, they are identical
    if not root1 and not root2:
        return True
    
    # If one node is None and the other is not, they are not identical
    if not root1 or not root2:
        return False
    
    # Check if the values of the current nodes are equal
    if root1.value != root2.value:
        return False
    
    # Recursively check the left and right subtrees
    return (are_identical_trees(root1.left, root2.left) and
            are_identical_trees(root1.right, root2.right))

# Example usage:
# Construct two identical trees
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

# Check if the trees are identical
result = are_identical_trees(root1, root2)

# Print the result
if result:
    print("The trees are identical.")
else:
    print("The trees are not identical.")
