class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        lists = defaultdict(list)
        queue, ans, res = deque(), [], []
        
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                indegree[recipes[i]] += 1
                lists[ingredients[i][j]].append(recipes[i])
        
        for i in range(len(supplies)):
            indegree[supplies[i]] = 0
                
        for i in range(len(supplies)):
            if indegree[supplies[i]] == 0:
                queue.append(supplies[i])  
        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for n in lists[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        for i in ans:
            if i in recipes:
                res.append(i)
        
        return res
                