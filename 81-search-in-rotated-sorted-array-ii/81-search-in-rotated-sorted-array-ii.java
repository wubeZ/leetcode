class Solution {
    
    public static boolean binarySearch(int left, int right, int target,int[] nums){
        while (left <= right){ 
        int mid = left + (right - left)/2;
        if(nums[mid]==target) return true;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
        }
        return false;    
    }
    
    public boolean search(int[] nums, int target) {
        int index = 0;
        for(int i=1; i<nums.length;i++){
            if(nums[i-1] > nums[i]){
                index = i;
                break;}
        }
        return binarySearch(0, index-1,target,nums) || binarySearch(index, nums.length-1,target,nums);
        
    }
    
}