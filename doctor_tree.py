class DoctorNode:
    def __init__(self, name):
        """Represents a single doctor in the tree."""
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        """Initializes an empty doctor tree."""
        self.root = None

    def insert(self, parent_name, child_name, side):
        """
        Inserts a new DoctorNode as the left or right report of the given parent.
        side should be either 'left' or 'right'.
        """
        if not self.root:
            print("Error: Cannot insert into an empty tree.")
            return

        parent_node = self._find(self.root, parent_name)
        if not parent_node:
            print(f"Error: Parent '{parent_name}' not found.")
            return

        if side == "left":
            if parent_node.left is None:
                parent_node.left = DoctorNode(child_name)
            else:
                print(f"Error: Left child of '{parent_name}' already exists.")
        elif side == "right":
            if parent_node.right is None:
                parent_node.right = DoctorNode(child_name)
            else:
                print(f"Error: Right child of '{parent_name}' already exists.")
        else:
            print("Error: Side must be 'left' or 'right'.")

    def _find(self, node, name):
        """Recursively searches for a DoctorNode by name."""
        if not node:
            return None
        if node.name == name:
            return node
        left_result = self._find(node.left, name)
        if left_result:
            return left_result
        return self._find(node.right, name)

    
    def preorder(self, node):
        """Root -> Left -> Right"""
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        """Left -> Root -> Right"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        """Left -> Right -> Root"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]

# Test your DoctorTree and DoctorNode classes here
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

    
    tree.insert("Dr. Unknown", "Dr. Test", "left")  
    tree.insert("Dr. Croft", "Dr. Stone", "middle")  

    Preorder: ['Dr. Croft', 'Dr. Phan', 'Dr. Morgan', 'Dr. Carson', 'Dr. Goldsmith']
Inorder: ['Dr. Morgan', 'Dr. Phan', 'Dr. Carson', 'Dr. Croft', 'Dr. Goldsmith']
Postorder: ['Dr. Morgan', 'Dr. Carson', 'Dr. Phan', 'Dr. Goldsmith', 'Dr. Croft']
Error: Parent 'Dr. Unknown' not found.
Error: Side must be 'left' or 'right'.



