from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        # pop other numbers then get it appended to the back
        for _ in range(len(self.queue) - 1):
            num = self.queue.popleft()
            self.queue.append(num)


    def pop(self) -> int:
        element = self.queue.popleft()
        return element

    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        # if not empty return false
        if len(self.queue) > 0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna