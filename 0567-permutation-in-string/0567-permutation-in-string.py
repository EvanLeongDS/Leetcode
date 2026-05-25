class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create the window for s1
        s1_dict = {}
        s1_len = len(s1)
        s2_len = len(s2)
        s2_dict = {}
        l = 0 
        r = s1_len - 1 

        # make sure s2 is actually bigger than s1
        if s1_len > s2_len:
            return False
        
        # add to the dictionary
        for i in range(s1_len):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)
            s2_dict[s2[i]] = 1 + s2_dict.get(s2[i], 0)
        print(s1_dict) 
        print(s2_dict)
        
        # check for first part of the window
        if s1_dict == s2_dict:
                return True 

        # iterate through the rest 
        for r in range(s1_len, s2_len):
            # add to s2 dictionary and slide the window 
            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r], 0)

            # remove everything out of the window and slide the window
            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]

            l += 1

            # check post slide 
            if s1_dict == s2_dict:
                return True 

        # we did not find a match, therefore return false 
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna