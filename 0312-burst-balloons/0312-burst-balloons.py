class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # build empty dp table
        n = len(nums)
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        # build base case 
        for i in range(1, n+1):
            dp[i][i+1] = 0
        print(dp)

        nums_padded = [1] + nums + [1]

        # gap loop
        for gap in range(2, n+2):
            for i in range(0, n+2-gap):
                j = i + gap
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums_padded[i]*nums_padded[k]*nums_padded[j])
        return dp[0][n + 1]