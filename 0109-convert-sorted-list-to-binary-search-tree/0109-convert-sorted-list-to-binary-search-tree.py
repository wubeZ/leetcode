# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
                    
        def create(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            
            node.left = create(arr[: mid])
            node.right = create(arr[mid + 1:])
            
            return node
            
        
        return create(arr)
            
            