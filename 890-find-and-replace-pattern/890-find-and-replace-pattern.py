class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        def checkPattern(word):
            res , seen = [], defaultdict(int)
            count = 0
            for i in range(len(word)):
                if word[i] in seen:
                    res.append(seen[word[i]])
                else:
                    count += 1
                    seen[word[i]] = count
                    res.append(seen[word[i]])
                           
            return res
            
        cpattern = checkPattern(pattern)
                
        for i in range(len(words)):
            wpattern = checkPattern(words[i])
            if wpattern == cpattern:
                ans.append(words[i])
        
        return ans