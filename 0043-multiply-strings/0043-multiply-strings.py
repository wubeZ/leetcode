class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        maps = {str(i):i for i in range(10)}
        arr1 = 0
        for i in range(len(num1)):
            arr1 = (arr1*10) + maps[num1[i]]
        arr2 = 0
        for i in range(len(num2)):
            arr2 = (arr2*10) + maps[num2[i]]
        
        return str(arr1 * arr2)