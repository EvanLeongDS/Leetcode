class StockSpanner:

    def __init__(self):
        # append tuples, do not brute force 
        self.stack = [] 

    def next(self, price: int) -> int:
        count = 1 
        if not self.stack:
            self.stack.append((price, 1))
            return 1

        # do a while loop  
        while self.stack and self.stack[-1][0] <= price:
            # increment count 
            count += self.stack.pop()[1]
        # add the temp count to the total count
        self.stack.append((price, count))
        return count 



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna