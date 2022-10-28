class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkWithPointers(s: str, i: int, one_pointer: bool) -> str:
            left = i
            right = i if one_pointer else i+1
                
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            poss1 = checkWithPointers(s, i, one_pointer=True)
            poss2 = checkWithPointers(s, i, one_pointer=False)
            longer = poss1 if len(poss1) > len(poss2) else poss2
            longest = longer if len(longer) > len(longest) else longest

        return longest
        