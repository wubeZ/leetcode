class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int [] result = new int [nums.length];
        int i = 0;    
        for(int j=0; j < nums.length; j++){
            if(nums[j] < pivot){
                result[i] = nums[j];
                i+=1;}}
        for(int k=0; k < nums.length; k++){
            if(nums[k] == pivot){
                result[i] = nums[k];
                i+=1;}}
        for(int l=0; l < nums.length; l++){
            if(nums[l] > pivot){
                result[i] = nums[l];
                i+=1;}}
        return result;
    }
}