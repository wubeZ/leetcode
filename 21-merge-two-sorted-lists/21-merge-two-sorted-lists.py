class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        pointer = list1
        spointer = list2
        
        
        while(pointer):
            answer.append(pointer.val)
            pointer = pointer.next
        while(spointer):
            answer.append(spointer.val)
            spointer = spointer.next
        answer.sort()
        
        if len(answer)==0:
            head = ListNode()
            head = None
            return head
    
        head = ListNode(answer[0])
        npointer = head
        
        i = 1
        while(len(answer) > i):
            nextNode = ListNode(answer[i])
            npointer.next = nextNode
            npointer = npointer.next
            i += 1
            
        return head