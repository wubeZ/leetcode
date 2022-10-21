class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrome_check(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(cur_idx, past_idx):
            if cur_idx == len(s):
                if path and past_idx == cur_idx:
                    ans.append(path[:])
                return 
            isvalid = palindrome_check(past_idx, cur_idx)
            
            if isvalid:
                path.append(s[past_idx:cur_idx+1])
                backtrack(cur_idx+1, cur_idx+1)
                path.pop()
            
            backtrack(cur_idx+1, past_idx)
            

        ans = []
        path = []
        backtrack(0, 0)
        
        return ans