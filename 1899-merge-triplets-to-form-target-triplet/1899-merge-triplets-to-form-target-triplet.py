class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        for triplet in triplets[:]:
            if all(t <= x for t, x in zip(triplet, target)):
                valid.append(triplet)

        best = [0, 0, 0]
        for triplet in valid:
            for i in range(len(triplet)):
                if triplet[i] > best[i]:
                    best[i] = triplet[i]
        if best == target:
            return True
        else:
            return False
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna