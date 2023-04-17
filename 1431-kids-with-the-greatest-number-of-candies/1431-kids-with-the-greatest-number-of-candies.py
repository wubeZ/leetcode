class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        
        res = []
        
        for candy in candies:
            value = ((candy + extraCandies) >= max_candy)
            res.append(value)
            
        return res