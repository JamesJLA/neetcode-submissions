class Solution {
public:

    string encode(vector<string>& strs) {
        string ret_str = "";
        for (string str : strs) {
            ret_str += to_string(str.length()) + "#" + str;
        }
        return ret_str;
    }

    vector<string> decode(string s) {
        vector<string> words;
        int i = 0;
        while (i < s.length()) {
            string lengthText;
            while (s[i] != '#') {
                lengthText += s[i];
                i++;
            }
            i++;

            int length = stoi(lengthText);
            string word;
            for (int j = 0; j < length; j++) {
                word += s[i];
                i++;
            }
            words.push_back(word);
        }
        return words;
    }
};
