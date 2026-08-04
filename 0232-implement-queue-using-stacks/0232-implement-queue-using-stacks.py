class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        # move the front number to the back so we can remove it 
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        final = self.stack2.pop()
        return final


    def peek(self) -> int:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna