class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;
        for (int num : numSet) {
            if (numSet.find(num-1) == numSet.end()) {
                int current = num;
                int consecutive = 1;

                while (numSet.find(current + 1) != numSet.end()) {
                    current++;
                    consecutive++;
                }
                if (consecutive > longest) {
                    longest = consecutive;
                }
            }
            
        }
        return longest;
    }
};
