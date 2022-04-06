class Solution {
    public int threeSumMulti(int[] arr, int target) {
        int result = 0;
        
        int i = 0;
        while(i < arr.length){
            int [] count = new int[101];
            int j = i + 1;
            while (j < arr.length){
                int k = target - arr[i] - arr[j];
                if( k >= 0 && k <= 100 && count[k] > 0){
                    result += count[k];
                    result %= (1000000007);}
                count[arr[j]] += 1;        
                j += 1;}
            i += 1;}
        
        return result;   
    }
}