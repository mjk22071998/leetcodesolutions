class Solution:
    def climbStairs(self, n: int) -> int:
        staircase = [1, 1, 2]
    
    
        for i in range(3, n+1):

            #calculating total number of ways to reach next staircase
            staircase.append(staircase[i-1] + staircase[i-2])


        #return total number of ways to reach n staircase
        return staircase[n]
        