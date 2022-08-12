class Solution {
public:
    double myPow(double x, long n) {
        if(n == 0){ return 1; }
        if(n < 0) { return 1/ myPow(x, (-1*n)); }       
        if(n%2 == 0){
            double res =  myPow(x, n/2); 
            return res * res; }
        else{return x * myPow(x, n-1);}
        
    }
};