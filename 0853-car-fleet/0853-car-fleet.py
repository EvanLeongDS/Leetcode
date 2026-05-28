class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # equation: time = (target - position) / speed
        stack = []

        # in descending order by position
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)
        
        for position, speed in cars:
            time = (target - position) / speed
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna