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
                    
        def create(l, r):
            if l >= r:
                if l == r:
                    return TreeNode(arr[r])
                return None
            
            mid = (l+r)//2
            node = TreeNode(arr[mid])
            
            node.left = create(l, mid - 1)
            node.right = create(mid + 1, r)
            
            return node
            
        
        return create(0, len(arr)-1)
            
            