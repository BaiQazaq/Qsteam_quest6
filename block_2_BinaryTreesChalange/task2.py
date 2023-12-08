# 2. Implement a method to convert a sorted array to a balanced binary search tree.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    # Create the root node with the middle element
    root = TreeNode(nums[mid])

    # Recursively construct the left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.key, end=" ")
        in_order_traversal(node.right)

# Example usage
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Convert the sorted array to a balanced BST
    bst_root = sorted_array_to_bst(sorted_array)

    # Perform in-order traversal to verify the BST
    print("In-order Traversal of Balanced BST:")
    in_order_traversal(bst_root)
