# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumReturn = None
        carry = 0
        
        while(l1 or l2):
                if l1 != None:
                     var1 = l1.val    
                else: 
                    var1 = 0
                if l2 != None:
                    var2 = l2.val
                else:
                    var2 = 0
                
                sumVal = var1 + var2 + carry
            
                if sumVal > 9:
                    sumVal = sumVal - 10
                    carry = 1
                else:
                    carry = 0

                resNode = ListNode(sumVal)

                if sumReturn == None:
                    sumReturn = resNode
                    last = resNode
                else:
                    last.next = resNode
                    last = resNode

                if l1:
                    l1 = l1.next
                if l2 :
                    l2 = l2.next

        if carry > 0:
            carryNode = ListNode(carry)
            last.next = carryNode
            last = carryNode

        return sumReturn 