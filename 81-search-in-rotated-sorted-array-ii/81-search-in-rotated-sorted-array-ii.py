class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        index = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                index = i
                break
        
        def binarySearch(left, right):
            while left <= right:
                mid = left + (right - left)//2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False
        
        return binarySearch(0, index-1) or binarySearch(index,len(nums)-1)





















        # nums.sort()
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             mid = left + (right - left)//2
            
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
            
#         return False