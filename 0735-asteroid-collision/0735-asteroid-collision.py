class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if stack and asteroid < 0 and stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
                # collision where asteroid is bigger than stack, keep the asteroid
                while stack and asteroid < 0 and stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                # check for equality before appending 
                if stack and asteroid < 0 and stack[-1] > 0 and abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                elif stack and abs(stack[-1]) > abs(asteroid) and asteroid < 0 and stack[-1] > 0 :
                    pass
                else:
                    stack.append(asteroid)
            elif stack and  asteroid < 0 and stack[-1] > 0 and abs(asteroid) < abs(stack[-1]):
                # collision where stack is bigger than asteroid, keep the stack
                pass
            elif stack and  asteroid < 0 and stack[-1] > 0 and abs(asteroid) == abs(stack[-1]):
                # collision where stack and asteroid are equal
                stack.pop()
            else:
                stack.append(asteroid)
        return stack


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna