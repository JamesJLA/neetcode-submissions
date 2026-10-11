class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> groups;

        unordered_map<string, vector<string>> words;
        for (int i = 0; i < strs.size(); i++) {
            string sorted = strs[i];
            std::sort(sorted.begin(), sorted.end());
            
            if (words.contains(sorted)) {
                words[sorted].push_back(strs[i]);
            }
            else {
                words[sorted] = {strs[i]};
            }
        }

        for (const auto& [key, value] : words) {
            groups.push_back(value);
        }

        return groups;
    }
};
