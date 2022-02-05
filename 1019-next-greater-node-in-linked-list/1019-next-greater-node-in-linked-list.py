# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        digits, stack = [], []
        pointer = head
        while(pointer):
            digits.append(pointer.val)
            pointer = pointer.next
        
        answer = [0]*len(digits)
        
        for i, val in enumerate(digits):
            while stack and val > digits[stack[-1]]:
                answer[stack.pop()] = val
            stack.append(i)

        return answer
    