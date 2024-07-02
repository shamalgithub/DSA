from binary_tree_theory import  TreeNode , BinaryTree
from collections import deque
"""
same binary tree - iterative solution

"""

class Solution:
    def is_same_tree(self , p:BinaryTree , q:BinaryTree)->bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        stack = deque([(p , q)])
        while stack:
            node1 , node2 = stack.pop()
            
            if node1.value == node2.value:
                
                if node1.right and node2.right:
                    stack.append((node1.right , node2.right))
                    
                # if node1.right or node2.right:
                #     return False
                
                if node1.left and node2.left:
                    stack.append((node1.left , node2.left))
                    
                # if node1.left or node2.left:
                #     return False
            else:
                return False
            
        return True
            







tree_1 = BinaryTree()
tree_1.add_node(1)
tree_1.add_node(2)
tree_1.add_node(4)

tree_2 = BinaryTree()
tree_2.add_node(1)
tree_2.add_node(2)
tree_2.add_node(7)

tree_1.display()
tree_2.display()

check  = Solution()
answer = check.is_same_tree(tree_1.root , tree_2.root)
print(answer)