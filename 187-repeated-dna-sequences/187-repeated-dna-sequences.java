class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        HashSet<String> visited = new HashSet<>();
        HashSet<String> ans = new HashSet<>();
        int left = 0;
        
        while (left < s.length()-9){
            String cur = "";
            
            for(int i= 0;i<10;i++){
                cur += s.charAt(i+left);
            }
            if (visited.contains(cur)){
                ans.add(cur);
            }
            visited.add(cur);
            left++ ;
        }
        return List.copyOf(ans);
        
        
        
    }
}