


class TreeNode:
    def __init__(self , value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    def add_node(self , value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.recursive_tree_travesal(self.root , value)
    
    def recursive_tree_travesal(self , node , value):
        if node.value > value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.recursive_tree_travesal(node.left , value)
        if node.value < value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.recursive_tree_travesal(node.right , value)
    
    
    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left is not None or node.right is not None:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")
    
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        # Swap the children for each parent
        temp_child = root.left
        root.left = root.right
        root.right = temp_child

        # Recursively invert the left and right subtrees
        self.invert_tree(root.left)
        self.invert_tree(root.right)
       
    
    def max_depth(self,root):
        if root is None:
            return 0
        else:
            return 1 + max(self.dfs(root.left), self.dfs(root.right))
        
    def dfs(self , root):
        if root is None:
            return 0
        else:
            left_depth = self.dfs(root.left)
            right_depth = self.dfs(root.right)
            return 1 + max(left_depth, right_depth)
         
        

    def display(self):
        self.print_tree(self.root)   
        
            
        
        
        
    

# Usage example
if __name__ == "__main__":
    tree = BinaryTree()
    values = [5, 3, 8, 2, 4, 7, 9]

    for value in values:
        tree.add_node(value)

    tree.display()
    
    tree.invert_tree(tree.root)
    tree.display()
    print(tree.max_depth(tree.root))
    

  

        
            