class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        max_price = 0

        # itereate through array and find the max price 
        while r < len(prices):
            # check if it qualifies and beats the max 
            if prices[r] > prices[l]:
                temp_price = prices[r] - prices[l] 
                if temp_price > max_price:
                    max_price = temp_price
            else: 
                # we know l > r therefore we can move l to r and establish that as a potentnial buy
                l = r
            # update the pointers 
            r += 1
        return max_price

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna