class Solution:
    def strStr(self, A: str, B: str) -> int:
        try:
            return A.index(B)
        except ValueError:
            return -1
        