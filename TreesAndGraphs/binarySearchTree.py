from binaryTree import TreeNode

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = TreeNode(None)
        
    def insert(self, key):
        new = TreeNode(key)
        if self.root.key is None:
            self.root = new
            return
        
        curr = self.root
        while curr:
            if curr.key > key:
                if curr.left is None:
                    curr.left = new
                    new.parent = curr
                    return
                curr = curr.left
            elif curr.key <= key:
                if curr.right is None:
                    curr.right = new
                    new.parent = curr
                    return
                curr = curr.right
                
    def get(self, key):
        curr = self.root
        while curr:
            if curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            elif curr.key <= key:
                curr = curr.right
            else:
                raise "Key not found"

if __name__ == "__main__":
    newTree = BinarySearchTree()
    newTree.insert(1)
    newTree.insert(2)
    newTree.insert(3)
    print(newTree.root.right.right.key)
    
            
            