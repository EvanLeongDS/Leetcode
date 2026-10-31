class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        # if the asteroid don't collide append to the stack
        stack.append(asteroids[0])

        for i in range(1, len(asteroids)):
            if stack and asteroids[i] < 0 and stack[-1] > 0:
                alive = True # a live asteroid means its hitting the stack
                while alive and stack and asteroids[i] < 0 and stack[-1] > 0: 
                    # we have a collision!
                    if abs(asteroids[i]) > abs(stack[-1]):
                        # asteroid destroys the top of the stack
                        stack.pop()
                    elif abs(asteroids[i]) == abs(stack[-1]):
                        # both the asteroid and the stack explode
                        stack.pop() 
                        alive = False
                    else:
                        alive = False
                    
                if alive:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
        return stack