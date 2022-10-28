class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int freq[128] = {0};
        int left = 0, right = -1;  // to ensure that the silding window [left, right] has no character at first
        int len = s.size(), ans = 0;
        while (left < len) {
            if (right + 1 < len && freq[s[right + 1]] == 0) {
                freq[s[++right]]++;
            } else {
                freq[s[left++]]--;
            }
            ans = max(right - left + 1, ans);
        }
        return ans;
    }
};