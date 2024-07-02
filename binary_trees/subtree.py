from binary_tree_theory import BinaryTree , TreeNode
from collections import deque
tree_1 = BinaryTree()
tree_1.add_node(5)
tree_1.add_node(3)
tree_1.add_node(7)
tree_1.add_node(1)
tree_1.add_node(4)
tree_1.add_node(6)
tree_1.add_node(8)

tree_2 = BinaryTree()
tree_2.add_node(3)
tree_2.add_node(1)
tree_2.add_node(4)

tree_1.display()
tree_2.display()

class Solution:
    
    
    # def is_same(self , tree:BinaryTree , subtree:BinaryTree) -> BinaryTree:
    #     tree_start = self.check_start(tree , subtree)
        
    #     if tree_start:
            
        
    
    
    def check_start(self , tree:BinaryTree , subtree:BinaryTree) -> BinaryTree:
        
        
        if tree is None or subtree is None:
            return False
        
        stack = deque()
        stack.append(tree.root)
        
        while stack :
            node = stack.pop()
            if node.value == subtree.value:
                tree = node
                break
            else:
                if node.right :
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        
            
        if tree:
            return self.is_identical_iterative(tree , subtree)
            
    # def is_identical_iterative(self, node1, node2):
    #     stack = deque([(node1, node2)])

    #     while stack:
    #         current1, current2 = stack.pop()

    #         if current1 is None and current2 is None:
    #             continue
    #         if  current1 is None or  current2 is None:
    #             return False
    #         if current1.value != current2.value:
    #             return False

    #         stack.append((current1.left, current2.left))
    #         stack.append((current1.right, current2.right))

        # return True
    def is_identical_iterative(self, node1, node2):
        stack = deque([(node1, node2)])
        are_identical = False  # Start with the assumption that trees are not identical

        while stack:
            current1, current2 = stack.pop()

            if current1 is None and current2 is None:
                continue
            if current1 is None or current2 is None:
                are_identical = False  # Set the flag to False when a mismatch is found
                break
            if current1.value != current2.value:
                are_identical = False  # Set the flag to False when a mismatch is found
                break

            stack.append((current1.left, current2.left))
            stack.append((current1.right, current2.right))

            are_identical = True  # Set the flag to True when no mismatches are found

        return are_identical 
                    
                    
            
    
    
        

solution  = Solution()
answer = solution.check_start(tree_1 , tree_2.root)
print(answer)