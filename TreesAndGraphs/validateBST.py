class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

def validateBST(root):
    def validate(root, min, max):
        if not root:
            return True
        if ((min and root.key < min) or (max and root.key >= max)):
            return False 
        return validate(root.left, min, root.key) and validate(root.right, root.key, max)
    return validate(root, None, None)
        
if __name__=="__main__":
    root = TreeNode(7)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    print(validateBST(root))
    