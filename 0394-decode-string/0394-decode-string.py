class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currString = ""
        currNum = 0 

        for i in range(len(s)):
            if s[i] == "[":
                # get the multiplier into the stack for the current string 
                stack.append([currString, currNum])
                # reset both
                currString, currNum = "", 0
            elif s[i] == "]":
                prevString = stack[-1][0]
                count = int(stack.pop()[1])
                currString = prevString + currString * count 
                print(currString)
            elif not s[i].isdigit():
                # add the word to the current string
                currString += s[i]
            else:
                # add to currNum
                currNum = currNum*10 + int(s[i])
        return currString


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna