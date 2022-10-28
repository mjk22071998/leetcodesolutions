class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        d = defaultdict(int)
        l, r = 0, 0
        while l <= r < len(s):
            if d[s[r]] == 1:
                d[s[l]] -= 1
                l += 1
            else:
                d[s[r]] += 1
                r += 1
            ans = max(ans, r-l)
        return ans

        