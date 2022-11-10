class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        
        ans = int(num) + 1
        result = []
        for n in str(ans):
            result.append(int(n))
        
        return result