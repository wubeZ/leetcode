# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        level = 0
        while q:
            arr = [node.val for node in q]
            if level %2 == 0:
                if arr[0]%2 == 0: return False
                for i in range(1,len(arr)):
                    if arr[i-1] >= arr[i] or arr[i-1]%2 == 0 or arr[i]%2 == 0:
                        return False
            else:
                if arr[0]%2 != 0: return False
                for i in range(1,len(arr)):
                    if arr[i-1] <= arr[i] or arr[i-1]%2 != 0 or arr[i]%2 != 0:
                        return False
            temp = deque()
            while q:
                cur  = q.popleft()
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            level += 1
            q = temp
        
        return True