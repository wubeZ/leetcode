class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            num = [str(i) for i in digits]
            ans  = int(''.join(num)) + 1
            res = [int(i) for i in str(ans)]
            return res
        else:
            digits[-1] = digits[-1] + 1
            return digits
        
        