class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for op in operations:
            if op not in ('+', 'C', 'D'):
                result.append(int(op))
            elif op == 'C':
                result.pop()
            elif op == 'D':
                temp = result[-1]
                result.append(int(2 * temp))
            elif op == '+':
                result.append(int(result[-1] + result[-2]))
        return sum(result)
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna