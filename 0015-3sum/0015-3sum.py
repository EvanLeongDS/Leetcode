class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # establish basic preprocessing
        nums = sorted(nums)
        print(nums)
        n = len(nums)
        output_list = []  

        # iterate through the three sum
        i = 0
        j = i + 1
        k = n - 1
        while i < n - 2:
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                i += 1 
                j = i + 1
                k = n - 1 
                continue
            while j < k: # hold nums[i] nums[j] stagnant test every k
                if nums[i] + nums[j] + nums[k] == 0:
                    output_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:  # skip duplicate j
                        j += 1
                    while j < k and nums[k] == nums[k-1]:  # skip duplicate k
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1 
            j = i + 1
            k = n - 1

        return output_list

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna