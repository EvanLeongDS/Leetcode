class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0 
        tens = 0
        twenties = 0 

        for bill in bills:
            diff = bill - 5
            # greedily take the biggest bill and if it doesn't work out return false 
            while twenties and diff >= 20:
                diff -= 20
                twenties -= 1
            while tens and diff >= 10:
                diff -= 10
                tens -= 1
            while fives and diff >= 5:
                diff -= 5
                fives -= 1

            if diff > 0:
                return False
            
            # add money to the bank
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
            else: 
                twenties += 1
        return True 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna