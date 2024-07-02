class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_iterative(root):
    if not root:
        return []
    
    result = []
    stack = []
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.val)
            current = current.right
    
    return result

def pre_order_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result

def post_order_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    visited = set()
    
    while stack:
        current = stack[-1]
        if current.left and current.left not in visited:
            stack.append(current.left)
        elif current.right and current.right not in visited:
            stack.append(current.right)
        else:
            visited.add(current)
            result.append(stack.pop().val)
    
    return result

def level_order_iterative(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

# Example usage
# Constructing a simple binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order:", in_order_iterative(root))
print("Pre-order:", pre_order_iterative(root))
print("Post-order:", post_order_iterative(root))
print("Level-order:", level_order_iterative(root))
