class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutive = 0 

        for number in nums_set:
            if number - 1 not in nums_set: 
                sequence = 0 
                # while there is a seuqence going increment i and sequence
                i = 0 
                while number + i in nums_set:
                    sequence += 1
                    i += 1
                if sequence > longest_consecutive:
                    longest_consecutive = sequence
        return longest_consecutive


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna