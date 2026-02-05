class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert_subtree(self, parent_data, subtree, left=True):
        parent = self._find_node(self.root, parent_data)
        if not parent:
            raise ValueError(f"Node {parent_data} not found")
        if left:
            parent.left = subtree.root
        else:
            parent.right = subtree.root

    def delete_subtree(self, node_data):
        if self.root is None:
            return
        if self.root.data == node_data:
            self.root = None
            return
        self._delete_helper(self.root, node_data)

    def _find_node(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        return self._find_node(node.left, data) or self._find_node(node.right, data)

    def _delete_helper(self, node, data):
        if node is None:
            return
        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return
        self._delete_helper(node.left, data)
        self._delete_helper(node.right, data)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


if __name__ == "__main__":
    root = Node(1)
    tree = BinaryTree(root)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)

    print("Original tree:")
    tree.inorder()
    print()

    sub_root = Node(10)
    subtree = BinaryTree(sub_root)
    subtree.root.left = Node(11)
    subtree.root.right = Node(12)

    tree.insert_subtree(3, subtree, left=True)
    print("After inserting subtree under node 3:")
    tree.inorder()
    print()

    tree.delete_subtree(2)
    print("After deleting subtree of node 2:")
    tree.inorder()
    print()
