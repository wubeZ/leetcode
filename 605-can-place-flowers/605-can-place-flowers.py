class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i==0 and (i+1) < len(flowerbed) and flowerbed[i+1]== 0:
                    flowerbed[i] = 1
                    n-=1
                elif (i+1) < len(flowerbed) and flowerbed[i-1]== 0 and flowerbed[i+1]== 0:
                    flowerbed[i] = 1
                    n-=1
                elif i == len(flowerbed)-1 and flowerbed[i-1]== 0:
                    flowerbed[i] = 1
                    n-=1
                
        
        return n <= 0
                    
            