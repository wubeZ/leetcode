# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode()
        temp = head
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i))
            
        if not heap:
            return
            
        while heap:
            if not head:
                head = lists[heap[0][1]]
            else:
                head.next = lists[heap[0][1]]
                head = head.next
                
            if lists[heap[0][1]].next:
                lists[heap[0][1]] = lists[heap[0][1]].next
                heapq.heapreplace(heap, (lists[heap[0][1]].val, heap[0][1]))
            else:
                heapq.heappop(heap)
                
        return temp.next