from binarySearchTree import BinarySearchTree
        
def successor(node):
    if node.right is not None:
        curr = node.right
        while curr:
            if curr.left is None:
                break
            curr = curr.left
        return curr
    
    parent = node.parent
    while parent:
        if node != parent.right:
            break
        node = parent
        parent = parent.parent
    return parent
    
        
        
def inorder(node, succ):
    if node:
        inorder(node.left, succ)
        if(node.key > succ.key):
            return node.key
        inorder(node.right, succ)
        
if __name__=="__main__":
    root = BinarySearchTree()
    root.insert(20)
    root.insert(8)
    root.insert(22)
    root.insert(4)
    root.insert(12)
    root.insert(10)  
    root.insert(14)    
    temp = root.root.left.right.right
    print(successor(temp).key)