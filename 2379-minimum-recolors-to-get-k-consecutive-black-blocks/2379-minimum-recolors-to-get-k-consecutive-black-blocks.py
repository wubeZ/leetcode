class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ans = float("inf")
        
        for i in range(len(blocks)- k + 1):
            j = 0
            count = 0
            while j < k:
                if blocks[i+j] == "W":
                    count += 1
                j += 1
                
            ans = min(ans, count)

        return ans