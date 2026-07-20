class Solution:
    def __init__(self):
        self.seen = set()
    def isHappy(self, n: int) -> bool:
        # endlessly in a cycle, probably a while loop!
        happy_sum = 0 
        while n > 0:
            digit = n % 10
            happy_sum += digit ** 2 
            n = n // 10 
        if happy_sum == 1:
            return True
        elif happy_sum in self.seen:
            return False
        else:
            self.seen.add(happy_sum) 
            return self.isHappy(happy_sum)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna