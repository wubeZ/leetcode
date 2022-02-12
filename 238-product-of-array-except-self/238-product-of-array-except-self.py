class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefMul = [1]
        mul = 1
        answer = []
        for val in nums[::-1]:
            mul *= val
            prefMul.append(mul)
        prefMul.pop()
        
        mul = 1
        for val in nums: 
            answer.append(mul * prefMul.pop())
            mul *= val
            
        return answer