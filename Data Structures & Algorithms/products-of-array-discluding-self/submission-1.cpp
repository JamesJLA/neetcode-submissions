class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left(nums.size());
        vector<int> right(nums.size());
        int left_total = 1;
        left[0] = 1;
        for (int i = 1; i < nums.size(); i++) {
            left_total *= nums[i-1];
            left[i] = left_total;
        }

        int right_total = 1;
        right[right.size()-1] = 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            right_total *= nums[i+1];
            right[i] = right_total;
        }

        vector<int> mults(nums.size());
        for (int k = 0; k < left.size(); k++) {
            mults[k] = left[k] * right[k];
        }

        return mults;
    }
};
