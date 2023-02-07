class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_size = 1
        
        basket = defaultdict(int)
        l = 0
        
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
            max_size = max(max_size, r - l + 1)
            
        return max_size