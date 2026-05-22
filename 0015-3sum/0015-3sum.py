class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # establish basic preprocessing
        nums = sorted(nums)
        print(nums)
        n = len(nums)
        output_list = []
        three_set = set()  
        # iterate through the three sum
        i = 0
        j = i + 1
        k = n - 1
        while i + 1 <= n:
            if nums[i] > 0:
                break
            while j < k: # hold nums[i] nums[j] stagnant test every k
                temp_tuple = tuple([nums[i], nums[j], nums[k]])
                if nums[i] + nums[j] + nums[k] == 0 and temp_tuple not in three_set:
                    output_list.append([nums[i], nums[j], nums[k]])
                    three_set.add(temp_tuple)
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