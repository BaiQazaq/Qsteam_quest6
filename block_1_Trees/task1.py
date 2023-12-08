# 1. Implement a binary tree in Python.
# 2. Write a program to find the height of a binary tree.
# 3. Create a function to perform an in-order traversal in a binary tree.
# 6. Design a function to insert a new node in a binary search tree.
# 7. Implement a method to search for a given value in a binary tree.
# 8. Create a program to find the minimum value in a binary search tree.
# 9. Write a function to delete a node from a binary search tree.


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if type(val) is int:
            if self.root:
                return self._find(val, self.root)
        elif type(val) is str:
            if self.root:
                return self._min_val(self.root)

    def _find(self, val, node):
        if val == node.v:
            return node.v
        elif val < node.v and node.l:
            return self._find(val, node.l)
        elif val > node.v and node.r:
            return self._find(val, node.r)
    
    def _min_val(self, node):
        if node.l.v:
            return self._min_val(node.l)
        else:
            return node.l.v

    def delete_tree(self):
        # garbage collector will do this for us.
        if self.root:
            self.root = None

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.l)
            print(node.v, end = " ")
            self._view_tree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(5)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.add(1)
tree.add(9)
tree.add(6)
tree.view_tree()
print()
# print(tree.find(3))
# print(tree.find(4))
print(tree.find("min"))
# tree.delete_tree()
# tree.view_tree()