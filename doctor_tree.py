
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        if self.root is None:
            raise ValueError("The tree is empty.")

        parent = self._find_node(self.root, parent_name)

        if parent is None:
            raise ValueError(f"Parent '{parent_name}' was not found.")

        if getattr(parent, side) is not None:
            raise ValueError(f"The {side} child is already occupied.")

        setattr(parent, side, DoctorNode(doctor_name))

    def _find_node(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node

        found = self._find_node(node.left, name)
        if found is not None:
            return found

        return self._find_node(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []
        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []
        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
