
"""
Linked list creatation code - Start 

"""

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
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " )
            current = current.next
        print("None")
        
        
"""
Linked list creation code - end 

"""

class AddTwoList():
    def add_two_list(self , l1:Node , l2:Node) ->Node:
        l1_current = l1.head
        l2_current = l2.head
        result = []
        if l1_current is None or l2_current is None:
            return None 
        
        remainder = 0
        
        while l1_current and l2_current:
           
            add = l2_current.data  + l1_current.data + remainder
            if add >= 10:
                q , mod = divmod(add , 10)
                remainder = q
                add = mod
            else:
                remainder = 0
                
            result.append(add)
            
            l2_current = l2_current.next
            l1_current = l1_current.next
        
            
        if l1_current is None:
            remaining_digits = l2_current
        else:
            remaining_digits = l1_current
        
        while remaining_digits :
            add = remainder + remaining_digits.data
            remaining_digits = remaining_digits.next
            
            if add >= 10:
                q , mod = divmod(add , 10)
                remainder = q
                add = mod
            else:
                remainder = 0
               
            result.append(add)
            
        
        if remainder > 0:
            result.append(remainder)
        
        
        added_list = LinkedList()   
        for r in result:
            added_list.append(r)
        
        return added_list
            
        
    

l1 = LinkedList()
l2 = LinkedList()

input_l1 = [9,9,9]
input_l2 = [9,9,9,9,9]

for i in input_l1:
    l1.append(i)

for i in input_l2:
    l2.append(i)





l1.display()
l2.display()

add = AddTwoList()
added_list = add.add_two_list(l1 , l2)
added_list.display()