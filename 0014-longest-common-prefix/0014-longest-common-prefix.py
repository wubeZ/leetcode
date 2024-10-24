class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        for w in strs:
            min_length = min(min_length, len(w))
            self.add(w)
        
        ans = []
        
        cur = self.root
        
        while len(cur.children) == 1:
            keys = list(cur.children.keys())
            key = keys[0] if keys else None
            if key:
                ans.append(key)
                cur = cur.children[key]
        
        return "".join(ans)[:min_length]