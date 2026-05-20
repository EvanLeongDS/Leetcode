import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-z0-9]', '', s.lower())
        n = len(cleaned_string)
        
        # indices 
        l = 0 
        r = n - 1 
        while l < r:
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l += 1
            r -= 1
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna