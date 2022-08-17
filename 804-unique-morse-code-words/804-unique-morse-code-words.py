class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = set()
        for word in words:
            res = []
            for char in word:
                res.append(d[ord(char) - 97])
            ans.add("".join(res))
        
        return len(ans)
                