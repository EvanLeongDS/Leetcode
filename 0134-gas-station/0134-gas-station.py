class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # iterate through it a negative cost 
        tank = 0 # how much is in the tank right now 
        start = 0 # starting index from which we can possibly make a full loop
        total_gas = 0 # gas leftover from driving through the entire loop once 
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total_gas += diff
            if tank < 0:
                # try a different starting point 
                start = i + 1
                tank = 0 
            print(tank, total_gas)

        # final checks and return statement 
        if total_gas < 0:
            return -1
        else:
            return start 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna