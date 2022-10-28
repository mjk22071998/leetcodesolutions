class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found=False
        l,r=0,len(nums)-1
        while l<=r:
            m=(r+l)//2
            if nums[m]==target:
                found=True
                break
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        if found:
            l,r=m,m
            while l>=0 and nums[l]==target :
                l-=1
            while r<len(nums) and nums[r]==target:
                r+=1
        return [-1,-1] if not found else [l+1,r-1]