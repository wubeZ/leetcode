class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashmap = Counter(words[0])
        
        
        for word in words:
            new_counter = Counter(word)
            deletekeys = []
            for k in hashmap:
                if k not in new_counter:
                    deletekeys.append(k)
                else:
                    hashmap[k] = min(hashmap[k], new_counter[k])
            for k in deletekeys:
                del hashmap[k]
                
        ans = []
        
        for k, v in hashmap.items():
            for _ in range(v):
                ans.append(k)
                
        return ans
                    
            