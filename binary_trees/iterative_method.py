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
tree_1.display()

class Solution:
    def interative_traversal(self , tree:BinaryTree):
        root = tree.root
        if root is None:
            return

        stack = deque()
        stack.append(root)

        while stack:
            node = stack.pop()
            print(node.value, end="->")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

solution = Solution()
answer = solution.interative_traversal(tree_1)