# 3. Create a function to find the lowest common ancestor of two nodes in a binary tree.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    # Base case: if the root is None or matches one of the target nodes
    if root is None or root.key == node1 or root.key == node2:
        return root

    # Recursively search in the left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # If both nodes are found in different subtrees, the current node is the LCA
    if left_lca and right_lca:
        return root

    # If one node is found, return that node as a potential LCA
    return left_lca if left_lca else right_lca

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    tree_root = TreeNode(3)
    tree_root.left = TreeNode(5)
    tree_root.right = TreeNode(1)
    tree_root.left.left = TreeNode(6)
    tree_root.left.right = TreeNode(2)
    tree_root.right.left = TreeNode(0)
    tree_root.right.right = TreeNode(8)
    tree_root.left.right.left = TreeNode(7)
    tree_root.left.right.right = TreeNode(4)

    # Example nodes to find the lowest common ancestor
    node1 = 5
    node2 = 1

    lca = find_lca(tree_root, node1, node2)
    print(f"The lowest common ancestor of nodes {node1} and {node2} is {lca.key}")
