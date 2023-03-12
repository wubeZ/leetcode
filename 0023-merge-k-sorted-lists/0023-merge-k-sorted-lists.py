# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(arr,(lists[i].val,i, lists[i]))
        
        dummy = ptr = ListNode()
        
        while arr:
        
            val, idx ,node = heapq.heappop(arr)
            ptr.next = node
            ptr = ptr.next
            node = node.next
            if node:
                heapq.heappush(arr, (node.val, idx ,node))
        
        return dummy.next
        
        