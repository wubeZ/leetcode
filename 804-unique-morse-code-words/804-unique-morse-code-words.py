class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = set()
        for i in range(len(words)):
            res = ""
            for j in range(len(words[i])):
                char = words[i][j]
                idx = ord(char) - ord("a")
                res += d[idx]
            ans.add(res)
        
        return len(ans)
                