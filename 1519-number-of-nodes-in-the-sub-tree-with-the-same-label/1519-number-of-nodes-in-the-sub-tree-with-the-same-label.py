class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(set)
        
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        
        ans = [0] * n
        
        def countlabels(node):
            if len(tree[node]) == 0:
                values = {labels[node] : 1}
                ans[node] = 1
                return values
            
            values = {}
            
            for child in tree[node]:
                tree[child].remove(node)
                dictionary = countlabels(child)
                for key in dictionary:
                    if key in values:
                        values[key] += dictionary[key]
                    else:
                        values[key] = dictionary[key]
            
            if labels[node] in values:
                values[labels[node]] += 1
            else:
                values[labels[node]] = 1
                
            ans[node] = values[labels[node]]
            
            return values
        
        
        countlabels(0)
        
        return ans