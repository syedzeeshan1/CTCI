

from binaryTree import BinaryTree

def first_common_ancestor(root, p, q):
        if not root or root == p or root == q:
            return root
        
        l = first_common_ancestor(root.left, p, q)
        r = first_common_ancestor(root.right, p, q)
        
        if l and r:
            return root
        
        return l or r
    

if __name__ == "__main__":
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)
    print(t.root.key, t.root.left.key, t.root.right.key, n2.left.key, n2.right.key, n3.left.key, n3.right, n4.left.key)
    ancestor = first_common_ancestor(t.root, n4, n2)
    print(ancestor.key)