# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        return self.reverse(cur_node)

    def reverse(self, cur_node, prev=None):
        if not cur_node:
            return prev
        next_node = cur_node.next
        cur_node.next = prev
        return self.reverse(next_node, cur_node)

             
