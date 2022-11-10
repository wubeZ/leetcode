class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        lists = list(s)
        ans = []
        def backtrack(idx, word):
            if idx > len(word):
                return
            ans.append("".join(word))
            for i in range(idx, len(s)):
                if not word[i].isnumeric():
                    temp = word[i]
                    if word[i].isupper():
                        word[i] = word[i].lower() 
                    else:
                        word[i] = word[i].upper()
                    backtrack(i+1, word)
                    word[i] = temp
        
        backtrack(0, lists)
        
        return ans