class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = TreeNode(None)
        
    def insert(self, key, parent=None):
        new = TreeNode(key)
        if parent is None:
            if self.root.key is None:
                self.root = new
                return new
            else:
                raise "root already exists"
        
        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise "no children more than 2"
        return new

if __name__ == "__main__":
    newTree = BinaryTree()
    n1 = newTree.insert(1, None)
    n2 = newTree.insert(2, n1)
    n3 = newTree.insert(3, n1)
    print(newTree.root.left.key)