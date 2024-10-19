class Solution:
    def kthCharacter(self, k: int) -> str:
        arr = "a"
        
        while len(arr) < k:
            curr = arr
            next_word = []
            for i in curr:
                ind = (ord(i) + 1) % 97
                chara = chr(97 + ind)
                next_word.append(chara)
            
            arr = curr + "".join(next_word)
        
        
        return arr[k-1]