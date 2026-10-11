#include<unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diffs;

        vector<int> pair = {};
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (diffs.contains(diff)) {
                 pair = {diffs[diff], i};
            }
            else {
                diffs[nums[i]] = i;
            }
        }
        return pair;
    }
};
