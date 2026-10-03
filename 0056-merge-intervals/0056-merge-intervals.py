class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # if interval[i][1] >= interval[i +1][0] merge it 
        # or if interval[0] <= interval[i+1][1]
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged_bank = []
        for interval in intervals:
             if not merged_bank:
                merged_bank.append(interval)
            
             if merged_bank and merged_bank[-1][1] >= interval[0]:
                merged_bank[-1][1] = max(interval[1], merged_bank[-1][1])

             else:
                merged_bank.append(interval)
        return merged_bank
