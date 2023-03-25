class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> s;
        int i = 0;
        int j = 0;
        
        while (i < m && j < n){
            if (nums1[i] > nums2[j]){
                s.push_back(nums2[j]);
                j++;
            }
            else{
                s.push_back(nums1[i]);
                i++;
            }   
        }
        
        while (i < m){
            s.push_back(nums1[i]);
            i++;
        }
        while (j < n){
            s.push_back(nums2[j]);
            j++;
        }
        
        for(int i = 0 ; i < m + n; i++){
            nums1[i] = s[i];
        }
    }
};