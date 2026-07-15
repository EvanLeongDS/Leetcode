class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        for i in range(int(len(hand) / groupSize)):
            smallest = min(hand)
            hand.remove(smallest)
            for j in range(groupSize - 1):
                increment = smallest + j + 1
                if increment not in hand: 
                    return False
                else: 
                    hand.remove(increment)
        return True
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna