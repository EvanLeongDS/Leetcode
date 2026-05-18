class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # sort the list 
        sort_list = sorted(nums)
        my_dict = {}

        previous_num = None
        frequency_counter = 0
        for i in sort_list:
            # if there is a number change add to dict and reset everything
            if i != previous_num:
                if previous_num is not None:
                    my_dict[previous_num] = frequency_counter
                frequency_counter = 0 
                previous_num = i
            frequency_counter += 1 

        # Add the last numbers frequency 
        if previous_num is not None:
            my_dict[previous_num] = frequency_counter
        
        # sort the dictionary and get the top k values 
        frequency_list = []
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_keys = list(sorted_dict.keys())

        return sorted_keys[:k]
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna