class Solution {
public:
    int kthGrammar(int n, int k) {
        if(n == 1){
         return 0;
        }
        if(n == 2){
        if(k == 1){
            return 0; 
        }
        return 1;
        }
    
        int length = pow(2, n-1);
        int mid = length / 2;
        
        if(k > mid){
            int res = kthGrammar(n - 1, k - mid);
            
            if(res == 0){
                return 1;    
            }
                return 0;
        }
        else{
            return kthGrammar(n - 1, k);
        }
    }
};