class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)
    
        def find(x):
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            
            if x != y: 
                if rank[x] >= rank[y]:
                    rank[x] += rank[y]
                    parent[y] = x
                else:
                    rank[y] += rank[x]
                    parent[x] = y
                
        email_list = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email in email_list:
                    union(i, email_list[email])
                else:
                    email_list[email] = i
        
        res = defaultdict(list)
        for email , key in email_list.items():
            rootkey = find(key)
            res[rootkey].append(email)
            
        ans = []       
        for idx , emails in res.items():
            ans.append([accounts[idx][0]])
            ans[-1].extend(sorted(emails))
            
        return ans
        
            
            
        
        
        