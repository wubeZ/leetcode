class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        lists = defaultdict(list)
        queue, ans = deque(), []
        
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                indegree[recipes[i]] += 1
                lists[ingredients[i][j]].append(recipes[i])
                
        for i in range(len(supplies)):
            queue.append(supplies[i])  
            
        recipes = set(recipes)
        
        while queue:
            cur = queue.popleft()
            if cur in recipes:
                ans.append(cur)
            
            for n in lists[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        return ans
                