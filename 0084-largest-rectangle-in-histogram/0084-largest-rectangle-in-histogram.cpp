class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        
        int n = heights.size();
        vector<int> stack;
        
        int ans = 0;
        
        for(int i = 0; i < n; i ++){
            while(!stack.empty() && (heights[stack.back()] > heights[i])) {
                int top = stack.back();
                stack.pop_back();
                
                int left = -1;
                if(!stack.empty()){
                    left = stack.back();
                }
                
                int length = heights[top];
                int width = i - left - 1;
                
                int area = length * width;
                ans = max(ans, area);
            }
            stack.push_back(i);
        }
        
        return ans;
    }
};