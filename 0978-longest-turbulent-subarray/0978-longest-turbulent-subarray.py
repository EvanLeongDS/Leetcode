class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #base case 
        if len(arr) == 1:
            return 1
        max_subarray = 1 # final return variable 
        current_subarray = 1
        n = len(arr)
        prev = None # tracks whether you have turbulence or not

        for k in range(1, n):
            if arr[k] > arr[k - 1]:
                # add if the previous turbulent was < 
                if prev == "<":
                    current_subarray += 1
                else:
                    current_subarray = 2
                prev = ">"
            elif arr[k] < arr[k -1]:
                # add if the previous turbulent was > 
                if prev == ">":
                    current_subarray += 1
                else:
                    current_subarray = 2
                prev = "<"
            else:
                current_subarray = 1
                prev = None
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna