class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digi_str = str(int("".join([str(i)for i in digits])) + 1)
        return [int(digi_str[i]) for i in range(len(digi_str))]
        