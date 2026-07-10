class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        bigsum = sum(nums)
        if (bigsum + target) % 2 != 0 or bigsum < abs(target):
            return 0
        P = (bigsum + target) // 2

        m = len(nums)
        n = P                       # amount axis now runs 0..P
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        # build table
        for i in range(1, m+1):
            for j in range(n+1): # j is a target, target gets progressively smaller as you build from the top down
                dp[i][j] = dp[i-1][j] # consider everything we have alrready done

                # add onto the "use" branch
                if nums[i-1] <= j:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
        return dp[m][n]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna