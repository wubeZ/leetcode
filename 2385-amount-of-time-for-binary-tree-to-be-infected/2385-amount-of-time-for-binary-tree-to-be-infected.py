# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left:
                graph[left.val].add(node.val)
                graph[node.val].add(left.val)
            if right:
                graph[right.val].add(node.val)
                graph[node.val].add(right.val)
            
            return node
        
        
        dfs(root)
        
        queue = deque()
        queue.append(start)
        
        dis = -1
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                for next_node in graph[cur]:
                    graph[next_node].discard(cur)
                    queue.append(next_node)
            dis += 1
        
        return dis