import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # establish some basic if statements
        if amount == 0:
            return 0 
        
        # establish the dp table
        n = amount + 1 # we want to build from 0 to the amount
        dp = [math.inf] * n
        dp[0] = 0


        # build the dp table 
        # take it or don't take it type shi 
        for i in range (1, n):
            for coin in coins:
                if coin <= i: # if the coin is too big there is no point in using it 
                    dp[i] = min(1 + dp[i - coin], dp[i])
        
        
        if dp[n -1] != math.inf:
            return dp[n-1]
        else:
            return -1