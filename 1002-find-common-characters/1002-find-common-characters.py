class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashmap = Counter(words[0])
        
        
        for word in words:
            new_counter = Counter(word)
            
            for k in hashmap:
                hashmap[k] = min(hashmap[k], new_counter[k])
                
        ans = []
        
        for k, v in hashmap.items():
            for _ in range(v):
                ans.append(k)
                
        return ans
                    
            