class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # dictionary tracks which characters won't belong 
        max_freq = 0 
        l = 0 
        longest = 0 

        for r in range(len(s)):
            # add to the dictionary
            count[s[r]] = 1 + count.get(s[r], 0)
            # find the most frequently appearing character
            max_freq = max(max_freq, count[s[r]])
            # if we reach the limit then shrink the limit 
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r-l + 1)
        return longest
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna