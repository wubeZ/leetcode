class Solution {
    public boolean isPalindrome(int x) {
        String input = String.valueOf(x);
        char [] ch = input.toCharArray(); 
        String reverse = "";
        for (int i= ch.length-1;i >= 0;i--){
            reverse += ch[i];}
        
        if (input.equals(reverse)){
            return true;}
        return false;  
    }
}