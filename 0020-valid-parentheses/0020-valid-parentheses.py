class Solution:
    def isValid(self, s: str) -> bool:
        # an odd number in s means it can't be true
        if len(s) % 2 != 0:
            return False
        # treat a list as a stack
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if len(stack) == 0:
                    return False
                top = stack.pop() # save for comparison

                if i == ")" and top != "(":
                    return False
                if i == "]" and top != "[":
                    return False
                if i == "}" and top != "{":
                    return False
        if len(stack) > 0:
            return False
        return True
        
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna