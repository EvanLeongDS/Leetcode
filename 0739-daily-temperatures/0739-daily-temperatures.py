class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = ([0] * len(temperatures))
        for index, i in enumerate(temperatures):

            # check the number of days by popping off the stack on a warm day
            while stack and i > temperatures[stack[-1]]:
                past_index = stack.pop()
                distance = index - past_index
                output[past_index] = distance
            stack.append(index)
        return output
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna