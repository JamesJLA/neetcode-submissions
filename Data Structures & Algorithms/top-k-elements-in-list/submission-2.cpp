class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }
        
        vector<pair<int, int>> num_counts;

        for (const auto& [key, value] : counts) {
            num_counts.push_back({value, key});
        }

        sort(num_counts.begin(), num_counts.end());

        vector<int> ret = {};
        int j = 0;
        for (int i = num_counts.size() - 1; j < k; i--) {
            ret.push_back(num_counts[i].second);
            j++;
        }

        return ret;
    }
};
