class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                temp = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif i == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1 - num2 
                stack.append(temp)
            elif i == "*":
                temp = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif i == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                temp = int(num1 / num2)
                stack.append(temp)
            else:
                stack.append(int(i))
        return stack[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna