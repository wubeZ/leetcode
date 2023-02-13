# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = list1

        ptr = dummy
        idx = 0
        
        for i in range(a):
            ptr = ptr.next
            
        start = ptr
        
        for i in range(a, b+1):
            ptr = ptr.next
        
        end = ptr.next
        
        start.next = list2
        
        ptr2 = list2
        while ptr2.next:
            ptr2 = ptr2.next
        
        ptr2.next = end
        
        
        return dummy.next
        
            