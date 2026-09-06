# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        
        temp = head 
        if not head:
            return 

        while head:
            hook = head
            try:
                while head.next.next: 
                    head = head.next 
            except:
                break
        
            tail = head.next
            head.next = None
            tail.next, head = hook.next, hook.next
            hook.next = tail 
            hook = head
            
        while temp: 
            print(temp.val)
            temp = temp.next
            