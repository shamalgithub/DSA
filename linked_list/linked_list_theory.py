class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        # current.next = self.recursive_traversal(current)
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " )
            current = current.next
        print("None")
        
    def recursive_traversal(self , node):
        if node.next is None:
            return node
        else:
            print(node.data)
            self.recursive_traversal(node.next)

my_list = LinkedList()

# Append elements to the linked list
my_list.append(5)
my_list.append(10)
my_list.append(15)
my_list.append(20)

# Display the linked list
my_list.display()