class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        XOR_sum = 0 
        # obtain subsets 

        subset_list = []
        subset = []

        def create_subset(i):
            if i == len(nums):
                subset_list.append(subset[:])
                return
            
            subset.append(nums[i])
            create_subset(i+1)

            subset.pop()
            create_subset(i+1)

        create_subset(0)

        print(subset_list)
        for subset in subset_list:
            temp_sum = 0
            if len(subset) == 0:
                pass
            if len(subset) == 1:
                XOR_sum += subset[0]
            else:
                for i in range(len(subset)):
                    temp_sum = temp_sum ^ subset[i]
            XOR_sum += temp_sum
            print(temp_sum, XOR_sum)
        return XOR_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna