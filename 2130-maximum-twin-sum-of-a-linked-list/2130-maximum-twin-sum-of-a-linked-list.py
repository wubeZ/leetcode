# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pointer = head
        list_OfNodes  =  []
        max_sum = 0
        while head:
            list_OfNodes.append(head)
            head=head.next
        
        left = 0
        right = len(list_OfNodes)-1
        
        while left <= right:
            result  =  list_OfNodes[left].val + list_OfNodes[right].val
            max_sum = max(max_sum ,result)
            left += 1
            right -= 1
            
        return max_sum