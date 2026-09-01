class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        currNum = 0 

        for i in range(len(s)):
            if s[i] == "[":
                # add current string and number to the stack 
                stack.append((currStr, currNum))

                # reset string and num 
                currStr = ""
                currNum = 0
            elif s[i] == "]":
                # pop the top item off the stack and get it into currStr
                poppedStr, poppedNum = stack.pop()
                currStr = poppedStr + poppedNum * currStr
            elif s[i].isdigit():
                # update currNum
                currNum = currNum * 10 + int(s[i])
            else:
                # update currStr
                currStr = currStr + s[i]
        return currStr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna