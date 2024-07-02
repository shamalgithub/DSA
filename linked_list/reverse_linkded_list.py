# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
        
class Solution:
    def __init__(self) -> None:
        self.head = None
    
    def append_node(self , data):
        new_node = ListNode(data)
        if not self.head :
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
            
    def display(self):
        
        current = self.head
        while current:
            print(current.data , end=" => ")
            current = current.next
        print("None")
         
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        counter = 0
        while curr:
            
            temp = curr.next
            curr.next = prev
           
            prev = curr
            curr = temp
            
            
            
            
        self.head = prev
        # return prev
                
                
            

linked_list  = Solution()
linked_list.append_node(1)
linked_list.append_node(2)
linked_list.append_node(4)
linked_list.display()
linked_list.reverseList(linked_list.head)
linked_list.display()