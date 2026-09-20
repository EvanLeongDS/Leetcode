class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        check_list = []
        trust_count = {}

        for i in range(1, n+1):
            check_list.append(i)
        for person, trustee in trust:
            if person in check_list:
                check_list.remove(person)
            
            # add to dictionary
            if trustee not in trust_count:
                trust_count[trustee] = 1
            else:
                trust_count[trustee] += 1
        if not check_list:
            return -1
        elif trust_count.get(check_list[0], 0) < n - 1:
            return -1
        else:
            return check_list[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna