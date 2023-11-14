class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


def checkBalanced(root):
    def balance(root):
        if not root:
            return [0, True]
        left = balance(root.left)
        right = balance(root.right)
        isBalanced = (left[1] and right[1] and abs(left[0] - right[0]) <= 1)
        return [1 + max(left[0], right[0]), isBalanced]

    return balance(root)[1]


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    print(checkBalanced(root))
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.right.right.right = TreeNode(7)
    root.right = TreeNode(3)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    root.right.right.right.right = TreeNode(11)
    print(checkBalanced(root))
