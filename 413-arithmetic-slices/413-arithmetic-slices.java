class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length < 3){return 0;}
        ArrayList<Integer> ans = new ArrayList<>();
        
        for(int i = 0; i < nums.length-2; i++){
            int count = 1;
            int diff = nums[i+1] - nums[i];
            for(int j = i+1 ;j < nums.length; j++){
                if(nums[j] - nums[j-1] == diff){
                    count += 1;
                    if(count >= 3){ans.add(count);}}
                else{break;}
            }
        }
        
        return ans.size();
    }
}