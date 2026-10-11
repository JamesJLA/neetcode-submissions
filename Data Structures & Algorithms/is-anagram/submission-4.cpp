#include<unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) { return false; }
        std::unordered_map<char, int> s1;
        std::unordered_map<char, int> t1;

        for (int i = 0; i < s.length(); i++) {
            s1[s[i]]++;
            t1[t[i]]++;
        }
        
        return s1 == t1;
    }

};
