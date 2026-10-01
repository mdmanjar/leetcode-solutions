class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        int top=0;
        for(int i=1;i<nums.size();i++){
            if (nums[top]<=nums[i]){
                top+=1;
                nums[top]=nums[i];
            }
        }
        return top+1;
    }
};