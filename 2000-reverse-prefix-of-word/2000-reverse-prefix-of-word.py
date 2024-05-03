class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        ind = -1
        for i, elem in enumerate(word_list):
            if elem == ch:
                ind = i + 1
                break
        
        if ind == -1:
            return word
        
        res = (word_list[:ind])[::-1]
        res = "".join(res) + word[ind:]
                
        
        return res