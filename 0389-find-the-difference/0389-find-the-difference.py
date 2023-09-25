class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        ans = []
        for key in counter2:
            if key not in counter1 or counter1[key] != counter2[key]:
                ans.append((( counter2[key]- counter1[key] ) * key))
        
        return "".join(ans)