class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while(left<right){
            if (s.charAt(left) != s.charAt(right)){
                String lside  = s.substring(left,right);
                String rside = s.substring(left+1,right+1);
                return (isPalindrome(lside) || isPalindrome(rside));}
            left += 1;
            right -= 1;   
        }
        return true;
    }
    
    public static boolean isPalindrome(String str){
        int left = 0;
        int right = str.length() - 1;
        while(left<right){
            if (str.charAt(left) != str.charAt(right)){
                return false;}
            left += 1;
            right -= 1;   
        }
        return true;
    }
 }