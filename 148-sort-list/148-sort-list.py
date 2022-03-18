# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = head
        nums = []
        i = 0
        while cur:
            nums.append(cur.val)
            cur = cur.next
            
        nums.sort()
    
        while prev:
            prev.val = nums[i]
            prev = prev.next
            i += 1
        
        return head