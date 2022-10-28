class Solution:
    def mySqrt(self, x: int) -> int:
        count=1
        i=0
        while(count<=x):
            x=x-count
            count=count+2
            i=i+1
        return (i)


        