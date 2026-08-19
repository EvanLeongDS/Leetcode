class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        skip = False # if we get one of those subtractions we skip the letter after it 
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if i < len(s) - 1 and s[i] == "I" and s[i+1] == "V":
                count += 4
                skip = True
            elif i < len(s) - 1 and s[i] == "I" and s[i+1] == "X":
                count += 9
                skip = True
            elif i < len(s) - 1 and s[i] == "X" and s[i+1] == "L":
                count += 40
                skip = True
            elif i < len(s) - 1 and s[i] == "X" and s[i+1] == "C":
                count += 90
                skip = True  
            elif i < len(s) - 1 and s[i] == "C" and s[i+1] == "D":
                count += 400
                skip = True
            elif i < len(s) - 1 and s[i] == "C" and s[i+1] == "M":
                count += 900
                skip = True
            elif s[i] == "I":
                count += 1
            elif s[i] == "V":
                count += 5
            elif s[i] == "X":
                count += 10
            elif s[i] == "L":
                count += 50
            elif s[i] == "C":
                count += 100
            elif s[i] == "D":
                count += 500
            elif s[i] == "M":
                count += 1000
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna