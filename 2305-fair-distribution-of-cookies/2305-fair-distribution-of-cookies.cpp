class Solution {
public:
    
    int ans = INT_MAX;
    
    int distributeCookies(vector<int>& cookies, int k) {
        vector<int> arr(k, 0);
        backtrack(arr, cookies, 0, k);
        
        return ans;
        
    }
    
    void backtrack(vector<int>& arr, vector<int>& cookies,int index, int k){
        if(index == cookies.size()){
            int maxCount = 0;
            for(int i = 0; i < arr.size(); i++){
                if(maxCount < arr[i]){
                    maxCount = arr[i];
                }
            }
            ans = min(ans, maxCount);
            
            return;
        }
        
        for(int i = 0; i < k; i++){
            arr[i] += cookies[index];
            backtrack(arr, cookies, index + 1, k);
            arr[i] -= cookies[index];
        }
    }
};