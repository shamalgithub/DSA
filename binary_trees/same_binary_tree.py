from binary_tree_theory import  TreeNode , BinaryTree

"""
create a two binary trees 

"""

class Solution:
    def is_same_tree(self , p:BinaryTree , q:BinaryTree)->bool:
        if p is None and q is None:
            return True
        
        # If one node is None and the other isn't, they're not equal
        if p is None or q is None:
            return False
        
        # Compare values of the current nodes
        if p.value == q.value:
            # Recursively check left and right subtrees
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        else:
            return False







tree_1 = BinaryTree()
tree_1.add_node(1)
tree_1.add_node(2)
tree_1.add_node(4)

tree_2 = BinaryTree()
tree_2.add_node(1)
tree_2.add_node(10)
tree_2.add_node(100)

tree_1.display()
tree_2.display()

check  = Solution()
answer = check.is_same_tree(tree_1.root , tree_2.root)
print(answer)