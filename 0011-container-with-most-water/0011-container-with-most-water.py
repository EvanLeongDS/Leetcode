class Solution:
    def maxArea(self, height: List[int]) -> int:
        # you need to take the min height between height[i] height[j] because # "that' how water works"
        max_area = 0 
        n = len(height)
        l = 0 
        r = n - 1 

        # calculate area 
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            # adjust
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna